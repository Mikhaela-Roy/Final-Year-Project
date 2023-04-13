#include <SoftwareSerial.h>
SoftwareSerial HC05(11,12);

#define ENCA1 2 //Motor A Encoders
#define ENCA2 7 // Motor A Encoders
#define ENCB1 4 // Motor B Encoders
#define ENCB2 2 // Motor B Encoders
#define PWM 5
#define AIN2 5 //Frowards Motor A
#define AIN1 10 //Backwards Motor A
#define BIN2 9 //Backwards Motor B
#define BIN1 6 //Forwards Motor B
 
int pos = 0;
String myCmd;

void setup() {
  HC05.begin(9600);
  pinMode(ENCA1,INPUT);
  pinMode(ENCA2,INPUT);
  pinMode(ENCB1,INPUT); 
  pinMode(ENCB2,INPUT);
  attachInterrupt(digitalPinToInterrupt(ENCA1),readEncoder,RISING);
  attachInterrupt(digitalPinToInterrupt(ENCB1),readEncoder,RISING);
  attachInterrupt(digitalPinToInterrupt(ENCA2),readEncoder,RISING);
  attachInterrupt(digitalPinToInterrupt(ENCB2),readEncoder,RISING);
}
 
void loop() {
  
  setMotor("RIGHT", 25, PWM, AIN2, BIN1); 
}
 
void setMotor(String myCmd, int pwmVal, int pwm, int in1, int in2){
    
    analogWrite(pwm,pwmVal);

    if(myCmd == "STRAIGHT"){ //STRAIGHT
      digitalWrite(in1, HIGH);
      digitalWrite(in2, HIGH);
    }
    if(myCmd == "RIGHT"){ //LEFT
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
    }
    if(myCmd == "LEFT"){ //RIGHT
      digitalWrite(in1, LOW);
      digitalWrite(in2, HIGH);
    }  
  
}
 
void readEncoder(){
  int b = digitalRead(ENCB1);
  if(b > 0){
    pos++;
  }
  else{
    pos--;
  }
}