#define F_CPU 16000000UL

#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>

// Local filesm
#include "uart.c"
#include "reciever.c"

void adc_init(void){
  ADCSRA |= _BV(ADPS2) | _BV(ADPS1) | _BV(ADPS0);    //Prescaler at 128 so we have an 125Khz clock source
  ADMUX |= _BV(REFS0);
  ADMUX &= ~_BV(REFS1);//Avcc(+5v) as voltage reference
  ADCSRA |= _BV(ADEN); //Power up the ADC
}

int main (void)
{
  uart_init(); // Initialize uart
  adc_init();
  sei(); // Enable global interrupts

  DDRB |= _BV(DDB5); // Pin 13 output

  DDRC &= ~_BV(DDC0); // Analog pin 0 input

  while(1) {
    ADCSRA |= _BV(ADSC);
    loop_until_bit_is_set(ADCSRA, ADSC);

    float temp = (((float)ADCW * 5000 / 1024) - 500) / 10;
    send_float(temp);

    //send_success();
    _delay_ms(5000);
  }
  return 0;
}
