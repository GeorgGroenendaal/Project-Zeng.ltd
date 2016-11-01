#define F_CPU 16000000UL

#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>

// Local files
#include "uart.c"
#include "protocol.c"

int main (void)
{
  uart_init(); // Initialize usart

  sei(); // Enable global interrupts

  DDRB |= _BV(PB2);

  while(1) {
    _delay_ms(100);
    PORTB ^= _BV(PB2);
    _delay_ms(100);
  }
  return 0;
}
