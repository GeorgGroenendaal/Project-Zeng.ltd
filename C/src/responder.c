/* This files defines functions for the response codes that the arduino can send
 * as defined in the communication protocoll
 */

// Sends array of max 7 chars over the serial port. Is
void send_characters(char instr[7]){
  char i;
  for (i = 0; i < 7 ; i++){
    // Exit the loop when instruction has ended
    if (instr[i] == 0x03){
      loop_until_bit_is_set(UCSR0A, UDRE0);
      UDR0 = instr[i];
      break;
    }
    // Make sure system is able to transmit
    loop_until_bit_is_set(UCSR0A, UDRE0);
    UDR0 = instr[i];
  }
}

// builds an success response and sends it
void send_success(){
  char instr[3] = {0x02, 0x30, 0x03};
  send_characters(instr);
}

// builds an failed response and sends it
void send_failed(){
  char instr[] = {0x02, 0x31, 0x03};
  send_characters(instr);
}
