/* Functions as a linker for the protocoll
 */

// 0x41
void proto_isalive(){
  send_success();
}

// 0x42
void proto_gettemprature(){
  float temp = gettemp();
  send_float(temp);
}

// 0x43
void proto_getdistance(){
  float temp = getdistance();
  send_float(temp);
}

// 0x44
void proto_getlight(){
  send_failed();
}

// 0x45
void proto_rollout(){
  send_failed();
}

// 0x46
void proto_rollin(){
  send_failed();
}

// 0x47
void proto_rollto(){
  send_failed();
}

// 0x48
void proto_settempraturethreshold(){
  send_failed();
}

// 0x49
void proto_setlightthreshold(){
  send_failed();
}

// 0x4A
void proto_gettempraturethreshold(){
  send_failed();
}

// 0x4B
void proto_getlightthreshold(){
  send_failed();
}

// 0x4C
void proto_setmaxrollout(){
  send_failed();
}

// 0x4D
void proto_setminrollout(){
  send_failed();
}

// 0x4E
void proto_resetsettings(){
  send_failed();
}
