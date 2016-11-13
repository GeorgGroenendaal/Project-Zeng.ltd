/* Functions as a linker for the protocoll
 */

// 0x41 - Returns success, lets know that it is alive
void proto_isalive(){
  send_success();
}

// 0x42 - sends the current temprature in degree Celcius
void proto_gettemprature(){
  float temp = gettemp();
  send_float(temp);
}

// 0x43 - Sends the current distance in cm
void proto_getdistance(){
  float temp = getdistance();
  send_float(temp);
}

// 0x44 - Sends the current light intensity as float between 0 - 100
void proto_getlight(){
  float light = getlight();
  send_float(light);
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
  if (PROTO_PARAM.f >= -50 && PROTO_PARAM.f <= 120){
    settempthreshold(PROTO_PARAM.f);
    send_success();
  }
  else {
    send_failed();
  }
}

// 0x49 - Sets the light threshold between 0 - 100
void proto_setlightthreshold(){
  if (PROTO_PARAM.f >= 0 && PROTO_PARAM.f <= 100){
    setlightthreshold(PROTO_PARAM.f);
    send_success();
  }
  else {
    send_failed();
  }
}

// 0x4A - Returns the current temp threshold
void proto_gettempraturethreshold(){
  send_float(D_TEMPTHRESHOLD);
}

// 0x4B - Returns the current light threshold
void proto_getlightthreshold(){
  send_float(D_LIGHTTHRESHOLD);
}

// 0x4C - Sets the maximum rollout 0 - 170
void proto_setmaxrollout(){
  if (PROTO_PARAM.f >= 5 && PROTO_PARAM.f <= 170){
    setmaxrollout(PROTO_PARAM.f);
    send_success();
  }
  else {
    send_failed();
  }
}

// 0x4D - Sets the minimum rollout
void proto_setminrollout(){
  if (PROTO_PARAM.f >= 5 && PROTO_PARAM.f <= 170 && PROTO_PARAM.f < D_MAXROLLOUT){
    setminrollout(PROTO_PARAM.f);
    send_success();
  }
  else {
    send_failed();
  }
}

// 0x4E - Resets all the settings to the default.
void proto_resetsettings(){
  settempthreshold(25);
  setlightthreshold(80);
  setmaxrollout(170);
  setminrollout(5);

  send_success();
}
