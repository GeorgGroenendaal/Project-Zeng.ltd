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
  UCSR0B = _BV(RXEN0) | _BV(TXEN0);   // RX and TX setting
}

void uart_putchar(char c) {
    UDR0 = c;
}

char uart_getchar(void) {
    loop_until_bit_is_set(UCSR0A, RXC0); /* Wait until data exists. */
    return UDR0;
}
