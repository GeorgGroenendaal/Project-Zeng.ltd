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

// Global that contains the last parameter recieved by the protocoll
union Param {
  char chrs[4];
  float f;
} PROTO_PARAM;

// Current mode of execution 0, 1 or 2 (still, out, in)
char MODE;
// Value that to roll to with margin
float ROLL_TO;
float ROLL_TO_min;
float ROLL_TO_max;
// The current cached distance
float CURRENTDISTANCE;

// Local files
#include "functions/automat.c"
#include "functions/init.c"
#include "functions/sensor.c"
#include "functions/data.c"

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

  while(1) {
    _delay_ms(10);
    // Stores the distance in local var
    CURRENTDISTANCE = getdistance();
    checkbuttons();
    mode();

  }
  return 0;
}
