void function1(){
  PORTB |= _BV(PB5);
}

void function2(){
  PORTB &= ~_BV(PB5);
}
