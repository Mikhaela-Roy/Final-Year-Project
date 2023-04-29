#include <SoftwareSerial.h>
SoftwareSerial mySerial(11,12);

#define AIN1 5
#define AIN2 10
#define BIN1 6
#define BIN2 9

String cmd;

//NEED TO ADD SPEED OF THE MOTORS

void setup(){
  mySerial.begin(9600);
  Serial.begin(9600);
  //HC05.println("Bluetooth Ready");
  //bluetooth.print("Enter command: ");
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
}

void loop(){
  while(Serial.available()){ 
  }
  cmd = Serial.readStringUntil('\r');
  setMotor(cmd);
  
}

void setMotor(String cmd){

   if(cmd == "straight"){
      digitalWrite(5, HIGH);
      digitalWrite(6, HIGH);
      Serial.println("Recieved: Straight");
    }
    else if(cmd == "left"){
      digitalWrite(5, HIGH);
      digitalWrite(6, LOW);
      Serial.println("Recieved: Left");
    }
    else if(cmd == "right"){
      digitalWrite(5, LOW);
      digitalWrite(6, HIGH);
      Serial.println("Recieved: Right");
    }
    else{
      digitalWrite(5, LOW);
      digitalWrite(6, LOW);
      Serial.println("Recieved: Stop");
    }
}