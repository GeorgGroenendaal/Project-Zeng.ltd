/*
  Handles the communications protocoll.
  via interrupts.

*/
#include <avr/interrupt.h>

char instructionlength = 2;
char instruction[2];

void echoinstruction(void){
  UDR0 = '\n';
  UDR0 = instruction[2];
  UDR0 = instruction[1];
}

ISR(USART_RX_vect){
  char recievedbyte;
  recievedbyte = UDR0;

  if (recievedbyte == '*'){
    instructionlength = 2;
  }
  else if (recievedbyte == '\r' && instructionlength == 0){
    echoinstruction();
  }
  else if (instructionlength > 0){
    instruction[instructionlength] = recievedbyte;
    instructionlength = instructionlength - 1;
  }
}
