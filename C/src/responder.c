/* This files defines functions for the response codes that the arduino can send
 * as defined in the communication protocoll
 */

// Internal function Waits for empty buffer and sends char
void send_char(char ch){
  loop_until_bit_is_set(UCSR0A, UDRE0);
  UDR0 = ch;
}

// Sends array of max 7 chars over the serial port.
void send_success_param(char param[4], char length){
  // Opening
  send_char(0x02);
  // Success + param response code
  send_char(0x32);

  char i;
  for (i = 0; i < length ; i++){
    send_char(param[i]);
  }
  // Send end byte
  send_char(0x03);
}

// builds an success response and sends it
void send_success(){
  send_char(0x02);
  send_char(0x30);
  send_char(0x03);
}

// builds an failed response and sends it
void send_failed(){
  send_char(0x02);
  send_char(0x31);
  send_char(0x03);
}

// Converts a float to 4 bytes and sends it over the serial connection.
void send_float(float val){
  union Datafloat {
    float temprature;
    char param[4];
  } floatcontainer;

  floatcontainer.temprature = val;
  send_success_param(floatcontainer.param, 4);
}
