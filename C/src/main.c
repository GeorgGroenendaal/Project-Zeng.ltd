// Used for delay functions
#define F_CPU 16000000UL

#include <avr/io.h>
#include <util/delay.h>

void main (void)
{
  DDRB |= _BV(DDB2); // Set arduino port 10 as output

  // Infinite loop
  while(1) {
    PORTB |= _BV(PB2);
    _delay_ms(1000);
    PORTB &= ~_BV(PB2);
    _delay_ms(1000);
  }
}
