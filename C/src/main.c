#define F_CPU 16000000UL

#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>

// Local filesm
#include "uart.c"
#include "reciever.c"

int main (void)
{
  uart_init(); // Initialize uart

  sei(); // Enable global interrupts

  DDRB |= _BV(DDB5);

  while(1) {

  }
  return 0;
}
