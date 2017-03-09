
#include "Arduino.h"


uint8_t buf[8] = { 0 }; /* Keyboard report buffer */

// Toggle switch big pin definitions
int B_toggle_pins[5] = {A0,A1,A2,A3,A4};
uint8_t B_toggle_command[5] = {14,15,16,17,18};
bool B_toggle_VALS[5] = {false};

// Toggle switch small pin definitions
int S_toggle_pins[10] = {2,3,4,5,6,7,8,9,10,11};
uint8_t S_toggle_command[10] = {4,5,6,7,8,9,10,11,12,13};
bool S_toggle_VALS[10] = {false};

//Button pin definitions
int S_moment_pins[3] = {12,13,A5};
uint8_t S_moment_command[3] = {19,20,21};
bool S_moment_VALS[3] = {false};



// release key function
void releaseKey()
{
  buf[0] = 0;
  buf[2] = 0;
  Serial.write(buf, 8);	// Release key
  Serial.flush();
  delay(700);
}



//The setup function is called once at startup of the sketch
void setup()
{
// Setup serial communication
Serial.begin(9600);

//start up message
//Serial.println("Starting up USB SWITCH_BOX");

// Setup input pins
//Serial.println("Starting up B_toggle_pins");
for(int i=0; i<5; ++i){
	pinMode(B_toggle_pins[i], INPUT_PULLUP);
}

//Serial.println("Starting up S_toggle_pins");
for(int i=0; i<10; ++i){
	pinMode(S_toggle_pins[i], INPUT_PULLUP);
}

//Serial.println("Starting up S_moment_pins");
for(int i=0; i<2; ++i){
	pinMode(S_moment_pins[i], INPUT_PULLUP);
}

//Serial.println("Starting up COMPLETE");
delay(500);
}


bool check_Switch(int Switch_ID,bool Switch_VAL, uint8_t Switch_command){
	// Switch is found to be on
	if(digitalRead(Switch_ID)){
		// if switch was off before do key-press command
		if(Switch_VAL == false){
		    buf[2] = Switch_command;
		    Serial.flush();
		    Serial.write(buf, 8);	// Send keypress
		    releaseKey();

		}
		Switch_VAL = true;
	}
	else { // Switch is found to be off
		Switch_VAL = false;
	}
	return Switch_VAL;
}

// The loop function is called in an endless loop
void loop()
{

//// check all big toggle switches
//for(int i=0; i<10; ++i){
//B_toggle_VALS[i] = check_Switch(B_toggle_pins[i], B_toggle_VALS[i], B_toggle_command[i]);
//}

// check all the S_toggle switches
for(int i=0; i<10; ++i){
Serial.flush();
S_toggle_VALS[i]=check_Switch(S_toggle_pins[i], S_toggle_VALS[i], S_toggle_command[i]);
Serial.flush();
}
//
//// check all the S_moment switches
//for(int i=0; i<2; ++i){
//S_moment_VALS[i]=check_Switch(S_moment_pins[i], S_moment_VALS[i], S_moment_command[i]);
//}

}
