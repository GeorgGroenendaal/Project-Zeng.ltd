#define F_CPU 16000000UL

#include <avr/io.h>
#include <stdint.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <stdbool.h>

// Globals, get initialized in eeprom_init
float D_TEMPTHRESHOLD;
float D_LIGHTTHRESHOLD;
float D_MAXROLLOUT;
float D_MINROLLOUT;

// Local filesm
#include "functions/init.c"
#include "functions/sensor.c"

#include "responder.c"
#include "protocoll.c"
#include "reciever.c"


int main (void)
{
  eeprom_init(); // Load eeprom to ram, or initialize eeprom
  port_init(); // Initialize port data registers
  timer_init(); // Start 16 bit timer.
  uart_init(); // Initialize uart
  adc_init(); // Initialize ADC
  sei(); // Enable global interrupts

  PORTB |= _BV(PB3);

  while(1) {
    PORTB ^= _BV(PB2) | _BV(PB3) | _BV(PB4);
    _delay_ms(1000);
  }
  return 0;
}
