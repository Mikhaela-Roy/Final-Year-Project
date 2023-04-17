#include <SoftwareSerial.h>
SoftwareSerial HC05(11,12);

#define AIN1 5
#define AIN2 10
#define BIN1 6
#define BIN2 9

void setup(){
  Serial.begin(9600);
  HC05.begin(9600);
  HC05.println("Bluetooth Ready");
  Serial.print("Enter command: ");
}

void loop(){
  
  if(Serial.available()){
    String cmd = Serial.readStringUntil('\r');
    Serial.println(cmd);
    setMotor(cmd);
  }
}

void setMotor(String cmd){

   if(cmd == "straight"){
      digitalWrite(AIN1, HIGH);
      digitalWrite(BIN1, HIGH);
      Serial.println("Recieved: Straight");
    }
    else if(cmd == "left"){
      digitalWrite(AIN1, HIGH);
      digitalWrite(BIN1, LOW);
      Serial.println("Recieved: Left");
    }
    else if(cmd == "right"){
      digitalWrite(AIN1, LOW);
      digitalWrite(BIN1, HIGH);
      Serial.println("Recieved: Right");
    }
    else if(cmd == "stop"){
      digitalWrite(AIN1, LOW);
      digitalWrite(BIN1, LOW);
      Serial.println("Recieved: Stop");
    }
}