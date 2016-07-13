/*
  AnalogReadSerial
  Reads an analog input on pin 0, prints the result to the serial monitor.
  Graphical representation is available using serial plotter (Tools > Serial Plotter menu)
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.
*/


// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  pinMode(9, OUTPUT);
}

// the loop routine runs over and over again forever:


void loop() {
  // lights up bulb in proportion to the sensor value
  int sensorValue = analogRead(A0);
  analogWrite(9, 255);
 
  // print out the value you read:
  Serial.println(sensorValue);
  delay(150);        // delay in between reads for stability
  analogWrite(9,0);
  delay(sensorValue);
}



//
//void loop() {
//  // lights up bulb in proportion to the sensor value
//  int sensorValue = analogRead(A0);
//  analogWrite(9, ((sensorValue - 5)* 2));
//  delay(500);
//  
//  // read the input on analog pin 0:
// 
//  // print out the value you read:
//  Serial.println(sensorValue);
//  delay(1);        // delay in between reads for stability
//}



//void loop() {
//  // lights up bulb and then gradually decreases brightness
//  analogWrite(9, 255);
//  delay(500);
//  analogWrite(9, 200);
//  delay(500);
//  analogWrite(9, 120);
//   delay(500);
//  analogWrite(9, 60);
//   delay(500);
//  analogWrite(9, 0);
//   delay(500);
//  // read the input on analog pin 0:
//  int sensorValue = analogRead(A0);
//  // print out the value you read:
//  Serial.println(sensorValue);
//  delay(1);        // delay in between reads for stability
//}

// to view the printed out statements go to Tools > Serial Monitor
