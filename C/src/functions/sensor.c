/* Contains all the base sensor functions. Can be used across the program
 */

// Returns the current temprature in Celsius TODO: Add Analog channel pointer write
float gettemp(void){
  ADCSRA |= _BV(ADSC);
  loop_until_bit_is_clear(ADCSRA, ADSC);

  float temp = (((float)ADCW * 5000 / 1024) - 500) / 10;
  return temp;
}

float getdistance(void){
  PORTB |= _BV(PB0);
  _delay_us(10);
  PORTB &= ~_BV(PB0);

  loop_until_bit_is_set(PINB, PB1);
  TCNT1 = 0;
  loop_until_bit_is_clear(PINB, PB1);
  unsigned int count = TCNT1;
  float distance = ((float)count / 16) / 58;

  return distance;
}
