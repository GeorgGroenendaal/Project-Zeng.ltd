#define F_CPU 16000000UL

#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>

// Local filesm
#include "functions/init.c"
#include "functions/sensor.c"

#include "responder.c"
#include "protocoll.c"
#include "reciever.c"

int main (void)
{
  port_init(); // Initialize port data registers
  timer_init();
  uart_init(); // Initialize uart
  adc_init(); // Initialize ADC
  sei(); // Enable global interrupts

  while(1) {
  }
  return 0;
}
