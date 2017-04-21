#include "Arduino.h"

#define Button1_pin 2

int Button1_state = LOW;

int Button_pin[32] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16};
int Button_state[32] = {LOW};

long Last_Debounce_Time = 0;
long Debounce_Delay = 50;

bool First_Print = 1;
char last_char = 'START_CHAR';

//The setup function is called once at startup of the sketch
void setup() {
	Serial.begin(9600);
	digitalWrite(13, OUTPUT);
	pinMode(Button1_pin, INPUT);
	Serial.print("test 1:\n");
}


char get_char(char old_char) {
	Button1_state = digitalRead(Button1_pin);

	char new_char = 'E';

	if (Button1_state == HIGH) {
		new_char = 'a';
	}
	return new_char;
}


// The loop function is called in an endless loop
void loop() {

	if ((millis() - Last_Debounce_Time) > Debounce_Delay) {

		char in_char = get_char(last_char);

		if (in_char == 'E') {
			First_Print = 1;
		}
		else{
			if (in_char != last_char){
				First_Print = 1;
        last_char = in_char;
			}
			if (First_Print == 1) {
				Serial.println(in_char);
				First_Print = 0;
			}
		}
		Last_Debounce_Time = millis();
	}
}
