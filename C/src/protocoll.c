/* Functions as a linker for the protocoll
 */

// 0x41 - When called sends an succes message
void base_isalive(){
  send_success();
}

// 0x42 - When called sends the current temprature in floating point
void sensor_gettemp(){
  float temp = gettemp();
  send_float(temp);
}

void sensor_getdistance(){
  float temp = getdistance();
  send_float(temp);
}

// 0x43 - Turns led 13 on
void led13on(){
  PORTB |= _BV(PB5);
  send_success();
}

// 0x44 - Turns led 13 on
void led13off(){
  PORTB &= ~_BV(PB5);
  send_success();
}
