#define F_CPU 16000000UL

#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>

// Local files
#include "uart.c"
#include "reciever.c"

int main (void)
{
  uart_init(); // Initialize usart

  sei(); // Enable global interrupts

  DDRB |= _BV(PB5);

  while(1) {
  }
  return 0;
}
