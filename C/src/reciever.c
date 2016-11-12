/* Unpacks the recieved messages and calls the corresponding function according
 * the communication protocoll. Instructions start at decimal 0x41 (ASCII letter A), and increment from that point
 * Corresponding function indice can be calculated by: instruction - 0x41 = instruction index.
 */
#include <avr/interrupt.h>
#include <stdbool.h>
#include <string.h>

bool new_instruction = false; // Toggled on if the next byte is instruction
char instruction; // Contains instruction code
char parameter[4]; // 4 bytes with for a maximum of 32 bits storage. We keep big endian notation

// Array of function pointers, that gets called based on
void (*func_ptr[14])() = {
  // 0 - 0x41
  proto_isalive,
  // 1 - 0x42
  proto_gettemprature,
  // 2 - 0x43
  proto_getdistance,
  // 3 - 0x44
  proto_getlight,
  // 4 - 0x45
  proto_rollout,
  // 5 - 0x46
  proto_rollin,
  // 6 - 0x47
  proto_rollto,
  // 7 - 0x48
  proto_settempraturethreshold,
  // 8 - 0x49
  proto_setlightthreshold,
  // 9 - 0x4A
  proto_gettempraturethreshold,
  // 10 - 0x4B
  proto_getlightthreshold,
  // 11 - 0x4C
  proto_setmaxrollout,
  // 12 - 0x4D
  proto_setminrollout,
  // 13 - 0x4E
  proto_resetsettings
};

// Aligns the instruction with func_ptr indice. So 0x41 executes the first function.
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
  char recievedbyte;
  recievedbyte = UDR0;

  // New command, Trash previous and set instruction parameters
  if (recievedbyte == 0x02){
    reset_instruction();
    new_instruction = true;
    return;
  }
  // Byte is instruction code, update instruction parameters
  else if (new_instruction == true){
    instruction = recievedbyte;
    new_instruction = false;
    return;
  }
  // End of command, execute the current instruction parameters
  else if (recievedbyte == 0x03){
    execute_instruction();
    reset_instruction();
    return;
  }
  // Other bytes are parameters. TODO: create an better parameter storing system.
  else {
    int i;
    for (i = 0; i < 4; i++){
      if (parameter[i] == 0x00){
        parameter[i] = recievedbyte;
      }
    }
  }
}
