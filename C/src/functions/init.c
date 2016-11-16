/* Contains initializer functions
 */

 #define BAUD 9600
 #include <util/setbaud.h>
 #include <avr/eeprom.h>

void eeprom_init(){
  // Checks  if eeprom is already set, if true load the values in ram, otherwise reset to default
  if (eeprom_read_byte((uint8_t*)0x00) != (uint8_t)0x01){
    eeprom_write_byte((uint8_t*)0x00, 0x01);
    // Set temprature threshold
    eeprom_write_float((float*)0x01, 25);
    // Set light threshold
    eeprom_write_float((float*)0x05, 80);
    // Set max rollout
    eeprom_write_float((float*)0x09, 170);
    // set min rollout
    eeprom_write_float((float*)0x0D, 5);
  }
  // Load the values into ram
  D_TEMPTHRESHOLD = eeprom_read_float((float*)0x01);
  D_LIGHTTHRESHOLD = eeprom_read_float((float*)0x05);
  D_MAXROLLOUT = eeprom_read_float((float*)0x09);
  D_MINROLLOUT = eeprom_read_float((float*)0x0D);
}

/* Sets up data direction registers
*/
void port_init(void){
  DDRB |= _BV(DDB0); // Pin 8 output (trigger)
  DDRB &= ~_BV(DDB1); // Pin 9 input (echo )

  DDRB |= _BV(DDB2); // Pin 13 output Red led
  DDRB |= _BV(DDB3); // Pin 14 output Green led
  DDRB |= _BV(DDB4); // Pin 15 output Yellow led

  DDRD &= ~_BV(DDB5); // Pin 5 Input ROLLIN
  DDRD &= ~_BV(DDB6); // Pin 6 Input stop
  DDRD &= ~_BV(DDB7); // Pin 7 input stop

  DDRD |= _BV(DDB2); // Pin 2 motor
  DDRD |= _BV(DDB3); // Pin 3 motor
  DDRD |= _BV(DDB4); // Pin 4 motor
  DDRB |= _BV(DDB5); // Pin 13 motor


  DDRB |= _BV(DDB2); // Pin 13 output Red led
  DDRB |= _BV(DDB3); // Pin 14 output Green led
  DDRB |= _BV(DDB4);

  DDRC &= ~_BV(DDC0); // Analog pin 0 input Temprature
  DDRC &= ~_BV(DDC1); // Analog pin 1 input Light

}

/* Sets the timer and prescaler
 */
void timer_init(void){
  TCCR1B |= _BV(CS10); // prescaler 0 - use system clock
}

/* Sets up the usb with the most common configuration:
 * 8 bit size, no parity
 */
void uart_init(void){
  UBRR0H = UBRRH_VALUE;
  UBRR0L = UBRRL_VALUE;

  UCSR0A &= ~_BV(U2X0);

  UCSR0C = _BV(UCSZ01) | _BV(UCSZ00); // 8 bit data size
  UCSR0B = _BV(RXEN0) | _BV(TXEN0) | _BV(RXCIE0);   // RX and TX setting and Rx Tx interrupts
 }

/* Sets up the ADC for analog input 128 bit prescaler, manual mode and 5v reference
*/
void adc_init(void){
  ADCSRA |= _BV(ADPS2) | _BV(ADPS1) | _BV(ADPS0); // 128 prescaler
  ADMUX |= _BV(REFS0);
  ADMUX &= ~_BV(REFS1); // 5v mode
  ADCSRA |= _BV(ADEN); // Turn on
}
