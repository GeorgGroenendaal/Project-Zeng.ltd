/* Contains initializer functions
 */

 #define BAUD 9600
 #include <util/setbaud.h>

/* Sets up data direction registers
*/
void port_init(void){
  DDRB |= _BV(DDB5); // Pin 13 output

  DDRB |= _BV(DDB0); // Pin 8 output (trigger)
  DDRB &= ~_BV(DDB1); // Pin 9 input (echo )

  DDRC &= ~_BV(DDC0); // Analog pin 0 input
}

/* Sets the timer and prescaler
 */
void timer_init(void){
  TCCR1B |= _BV(CS10);
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
