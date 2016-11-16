/* Stores data from the application in the eeprom memory of the chip
  Adress mapping
  0x00  byte true or false based on wheter to reset eeprom
  0x01  float contains temprature threshold
  0x05  float contains light threshold
  0x09  float contains max rollout
  0x0D  float contains min rollout
 */

#include <avr/eeprom.h>

void settempthreshold(float temp){
  D_TEMPTHRESHOLD = temp;
  eeprom_write_float((float*)0x01, temp);
}

void setlightthreshold(float light){
  D_LIGHTTHRESHOLD = light;
  eeprom_write_float((float*)0x05, light);
}

void setmaxrollout(float rollout){
  D_MAXROLLOUT = rollout;
  eeprom_write_float((float*)0x09, rollout);
}

void setminrollout(float rollout){
  D_TEMPTHRESHOLD = rollout;
  eeprom_write_float((float*)0x0D, rollout);
}
