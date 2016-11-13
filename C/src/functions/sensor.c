/* Contains all the base sensor functions. Can be used across the program
 */

// Returns the current temprature in Celsius
float gettemp(void){
  ADMUX &= ~_BV(MUX0); // Set channel point to port 0
  ADCSRA |= _BV(ADSC); // Start adc measurement
  loop_until_bit_is_clear(ADCSRA, ADSC); // proceed when done

  float temp = (((float)ADCW * 5000 / 1024) - 500) / 10;
  return temp;
}

// Returns the current distance measured by the distance sensor in cm
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

// Returns the current light intensity as value between 0 - 100 - 0 being no light - 100 being maximum light
float getlight(void){
  ADMUX |= _BV(MUX0); // Set channel point to port 1
  ADCSRA |= _BV(ADSC); // Start adc measurement
  loop_until_bit_is_clear(ADCSRA, ADSC);  // proceed when done

  float vol = (float)ADCW / 1024 * 100;
  return vol;
}
