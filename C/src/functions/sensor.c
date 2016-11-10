/* Contains all the base sensor functions. Can be used across the program
 */

// Returns the current temprature in Celsius TODO: Add Analog channel pointer write
float gettemp(void){
  ADCSRA |= _BV(ADSC);
  loop_until_bit_is_clear(ADCSRA, ADSC);

  float temp = (((float)ADCW * 5000 / 1024) - 500) / 10;
  return temp;
}
