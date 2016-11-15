/* Contains autonimous functions
 */

 void setrollto(float rollto){
   ROLL_TO = rollto;
   ROLL_TO_max = rollto + 1;
   ROLL_TO_min = rollto - 1;
 }

void rollin(){
  int run;
  char i;
  for (run = 0; run < 500; run++){
    for (i = 0;i <= 3; i++){
      switch (i) {
        case 0:
          PORTD |= _BV(PD2);
          PORTD |= _BV(PD3);
          PORTD &= ~_BV(PD4);
          PORTB &= ~_BV(PB5);
        break;
        case 1:
          PORTD &= ~_BV(PD2);
          PORTD |= _BV(PD3);
          PORTD |= _BV(PD4);
          PORTB &= ~_BV(PB5);
        break;
        case 2:
          PORTD &= ~_BV(PD2);
          PORTD &= ~_BV(PD3);
          PORTD |= _BV(PD4);
          PORTB |= _BV(PB5);
        break;
        case 3:
          PORTD |= _BV(PD2);
          PORTD &= ~_BV(PD3);
          PORTD &= ~_BV(PD4);
          PORTB |= _BV(PB5);
        break;
      }
    _delay_ms(2);
    }
  }
}

void rollout(){
  int run;
  char i;
  for (run = 0; run < 500; run++){
    for (i = 3;i >= 0; i--){
      switch (i) {
        case 0:
          PORTD |= _BV(PD2);
          PORTD |= _BV(PD3);
          PORTD &= ~_BV(PD4);
          PORTB &= ~_BV(PB5);
        break;
        case 1:
          PORTD &= ~_BV(PD2);
          PORTD |= _BV(PD3);
          PORTD |= _BV(PD4);
          PORTB &= ~_BV(PB5);
        break;
        case 2:
          PORTD &= ~_BV(PD2);
          PORTD &= ~_BV(PD3);
          PORTD |= _BV(PD4);
          PORTB |= _BV(PB5);
        break;
        case 3:
          PORTD |= _BV(PD2);
          PORTD &= ~_BV(PD3);
          PORTD &= ~_BV(PD4);
          PORTB |= _BV(PB5);
        break;
      }
    _delay_ms(2);
    }
  }
}

void motor(){
  if (CURRENTDISTANCE < ROLL_TO_max && CURRENTDISTANCE > ROLL_TO_min){
    MODE = 0x00;
  }
  else if (CURRENTDISTANCE < ROLL_TO_max){
    MODE = 0x01;
    rollout();
  }
  else if (CURRENTDISTANCE > ROLL_TO_min){
    MODE = 0x02;
    rollin();
  }
}

// Updates the correct leds and activate correct mode
void mode(){
  if (MODE == 0x00){
    PORTB &= ~_BV(PB4);
    if (CURRENTDISTANCE < D_MINROLLOUT + 1){
      PORTB |= _BV(PB3);
      PORTB &= ~_BV(PB2);
    }
    else {
      PORTB &= ~_BV(PB3);
      PORTB |= _BV(PB2);
    }
    motor();
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

void checksensors(){
  if (gettemp() >= D_TEMPTHRESHOLD || getlight() >= D_LIGHTTHRESHOLD && MANUAL == false){
    setrollto(D_MAXROLLOUT);
  }
  else if (MANUAL == true){

  }
  else {
    setrollto(D_MINROLLOUT);
  }
}

// Checks if the user pushes buttons
void checkbuttons(){
  if (PIND & _BV(PD5) && PIND & _BV(PD7)){
    MANUAL = false;
    char i;
    for (i = 0; i < 5; i++){
      PORTB |= _BV(PB2);
      PORTB |= _BV(PB3);
      PORTB |= _BV(PB4);
      _delay_ms(250);
      PORTB &= ~_BV(PB2);
      PORTB &= ~_BV(PB3);
      PORTB &= ~_BV(PB4);
      _delay_ms(250);
    }
    setrollto(D_MINROLLOUT);
  }
  // Rollin
  else if (PIND & _BV(PD5)){
    MANUAL = true;
    setrollto(D_MINROLLOUT);
  }
  // Rollout
  else if(PIND & _BV(PD7)){
    MANUAL = true;
    setrollto(D_MAXROLLOUT);
  }
  // Stop
  else if(PIND & _BV(PD6)){
    MANUAL = true;
    setrollto(CURRENTDISTANCE);
  }
}
