#include "Arduino.h"

#define buttonPin 2

int buttonstate = LOW;
long lastDebounceTime = 0;
long debounceDelay = 50;
bool firstprint = 1;

//The setup function is called once at startup of the sketch
void setup() {
	Serial.begin(9600);
	digitalWrite(13, OUTPUT);
	pinMode(buttonPin, INPUT);
	Serial.print("test 1:\n");
	// Add your initialization code here
}

// The loop function is called in an endless loop
void loop() {

	buttonstate = digitalRead(buttonPin);

	if ((millis() - lastDebounceTime) > debounceDelay) {
		if (buttonstate == HIGH) {

			if (firstprint == 1) {
				Serial.print("a\n");
				firstprint = 0;
			}

			lastDebounceTime = millis();
		} else {
			firstprint = 1;

		}
	}
}
