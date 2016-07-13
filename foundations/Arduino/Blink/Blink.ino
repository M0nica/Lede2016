/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the Uno and
  Leonardo, it is attached to digital pin 12. If you're unsure what
  pin the on-board LED is connected to on your Arduino model, check
  the documentation at http://www.arduino.cc

  This example code is in the public domain.

  modified 8 May 2014
  by Scott Fitzgerald
 */
// Physical setup of Arduino
// pin 12 => resistor => LED => GDN
// pin 10 => resistor => a DIFFERENT LED => GND

// the setup function runs once when you press reset or power the board
// setup only runs once in Arduino
void setup() {
  // initialize digital pin 12 as an output.
  pinMode(12, OUTPUT);
  pinMode(10, OUTPUT);
}

// the loop function runs over and over again forever
// until you unplug Arduino this will continue running

//alternate the lights for 10 and 12
void loop() {
  digitalWrite(10, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(100);              // wait for a 1/2 second
  digitalWrite(10, LOW);    // turn the LED off by making the voltage LOW
  delay(500);              // wait for a 1/2 second between 10 and 12

  digitalWrite(12, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(100);              // wait for a 1/2 second
  digitalWrite(12, LOW);    // turn the LED off by making the voltage LOW
  delay(500);              // wait for a 1/2 second
}

//turn 10 and 12 on/off at the same time
//void loop() {
//  digitalWrite(10, HIGH);
//  digitalWrite(12, HIGH); // turn the LED on (HIGH is the voltage level)
//  delay(100);              // wait for a 1/2 second
//  digitalWrite(10, LOW);
//  digitalWrite(12, LOW); // turn the LED off by making the voltage LOW
//  delay(500);              // wait for a 1/2 second between 10 and 12
//
//}
