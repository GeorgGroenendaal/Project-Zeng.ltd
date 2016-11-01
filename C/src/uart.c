/*
  Sets up usb serial connection on the Arduino
*/
#define BAUD 9600
#include <util/setbaud.h>

/*
  Sets up the usb with the most common configuration:
  8 bit size, no parity
*/
void uart_init(void){
  UBRR0H = UBRRH_VALUE;
  UBRR0L = UBRRL_VALUE;

  UCSR0A &= ~(_BV(U2X0));

  UCSR0C = _BV(UCSZ01) | _BV(UCSZ00); // 8 bit data size
  UCSR0B = _BV(RXEN0) | _BV(TXEN0) | _BV(RXCIE0);   // RX and TX setting and Rx interrupts
}
