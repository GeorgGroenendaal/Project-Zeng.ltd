/* Contains autonimous functions
 */

void motor(){
  if (CURRENTDISTANCE < ROLL_TO_max && CURRENTDISTANCE > ROLL_TO_min){
    MODE = 0x00;
  }
  else if (CURRENTDISTANCE < ROLL_TO_max){
    MODE = 0x01;
  }
  else if (CURRENTDISTANCE > ROLL_TO_min){
    MODE = 0x02;
  }
}

// Updates the correct leds and activate correct mode
void mode(){
  if (MODE == 0x00){
    PORTB &= ~_BV(PB4);
    if (CURRENTDISTANCE <= D_MINROLLOUT){
      PORTB |= _BV(PB3);
      PORTB &= ~_BV(PB2);
    }
    else {
      PORTB &= ~_BV(PB3);
      PORTB |= _BV(PB2);
    }
  }
  else if (MODE == 0x01){
    PORTB |= _BV(PB2);
    PORTB &= ~_BV(PB3);
    PORTB |= _BV(PB4);
    motor();
  }
  else if (MODE == 0x02){
    PORTB |= _BV(PB3);
    PORTB &= ~_BV(PB2);
    PORTB |= _BV(PB4);
    motor();
  }
}

// Checkbuttons:
void checkbuttons(){

}

void setrollto(float rollto){
  ROLL_TO = rollto;
  ROLL_TO_max = rollto + 0.5;
  ROLL_TO_min = rollto - 0.5;
}
