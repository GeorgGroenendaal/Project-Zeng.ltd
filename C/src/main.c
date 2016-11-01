#define F_CPU 16000000UL

#include <avr/io.h>
#include <util/delay.h>

// Local files
#include "uart.c"

int main (void)
{
  uart_init();

  DDRB |= _BV(PB2);

  while(1) {

    char i = '.';
    uart_putchar(i);

    uart_getchar();
    PORTB ^= _BV(PB2);
  }
  return 0;
}
