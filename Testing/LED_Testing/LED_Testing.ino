#include <SoftwareSerial.h>
SoftwareSerial HC05(11,12);
String myCmd;

void setup() {
  // put your setup code here, to run once:
  HC05.begin(9600);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available()){
    pinMode(4, OUTPUT);
  }
  myCmd = Serial.readStringUntil('\r');
  
  if(myCmd == "ON"){
    digitalWrite(4, HIGH);
    Serial.println("Data recieved");
    
  }
  if(myCmd == "OFF"){
    digitalWrite(4, LOW);
    Serial.print("Data recieved");       
  }
}
