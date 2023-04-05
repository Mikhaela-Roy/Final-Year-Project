#include <SoftwareSerial.h>
SoftwareSerial HC05(10,11);
String myCmd;

void setup() {
  // put your setup code here, to run once:
  HC05.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  while(HC05.available()==0){
    pinMode(4, OUTPUT);
  }
  myCmd = HC05.readStringUntil('\r');
  
  if(myCmd == "LEFT"){
    digitalWrite(4, HIGH);
    Serial.print("Data recieved");
    
  }
  if(myCmd == "RIGHT"){
    digitalWrite(4, LOW);
    Serial.print("Data recieved");       
  }
}
