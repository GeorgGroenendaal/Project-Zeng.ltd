#include "responder.c"

// 0x41 - When called sends an succes message
void base_isalive(){
  send_success();
}

// 0x42 - Turns led 13 on
void led13on(){
  PORTB |= _BV(PB5);
  send_success();
}

// 0x43 - Turns led 13 on
void led13off(){
  PORTB &= ~_BV(PB5);
  send_success();
}
