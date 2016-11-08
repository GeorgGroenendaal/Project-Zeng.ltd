/* Unpacks the recieved messages and calls the corresponding function according
 * the communication protocoll
 */
#include <avr/interrupt.h>
#include <stdbool.h>
#include <string.h>

#include "function.c"

// Contains corresponding pointer to the function
void (*func_ptr[2])() = {
  function1,
  function2
};

// Instruction parameters
bool new_instruction = false;
char instruction;
// 4 bytes with for a maximum of 32 bits storage. We keep big endian notation
char parameter[4];

/* Peforms unpacking and executes corresponding function.
 * Instructions start at decimal 0x41 (ASCII letter A), and increment from that point
 * Corresponding function indice can be calculated by: instruction - 0x41 = instruction index
 */
void execute_instruction(){
  char index = instruction - 0x41;
  func_ptr[index]();
}

// Resets the instruction variables
void reset_instruction(){
  new_instruction = false;
  instruction = 0x00;
  memset(&parameter, 0x00, 4);
}

// Serial interrupt. Gets called when a byte over serial has been recieved.
ISR(USART_RX_vect){
  // Byte recieved trough usb
  char recievedbyte;
  recievedbyte = UDR0;

  UDR0 = recievedbyte;

  // 0x02 is a new command
  if (recievedbyte == 0x02){
    // Trash the previous instruction
    reset_instruction();
    // Set new_instruction parameter, so next byte is instruction byte
    new_instruction = true;
    return;
  }
  // Check if instruction byte
  else if (new_instruction == true){
    // Set the instruction
    instruction = recievedbyte;
    // Toggle the new_instruction flag to off, Next bytes will be parameters or
    // end of command
    new_instruction = false;
    return;
  }
  // End of command
  else if (recievedbyte == 0x03){
    execute_instruction();
    reset_instruction();
    return;
  }
  // All other situations are bytes
  else {
    int i;
    for (i = 0; i < 4; i++){
      if (parameter[i] == 0x00){
        parameter[i] = recievedbyte;
      }
    }
  }
}
