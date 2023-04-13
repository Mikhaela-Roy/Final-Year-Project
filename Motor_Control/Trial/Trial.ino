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
 
String myCmd;
int pos = 0;
int pwm = PWM;
int pmwVal;

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
  while(HC05.available() == 0){
    pinMode(AIN1,OUTPUT);
    pinMode(AIN2,OUTPUT);
    pinMode(BIN2,OUTPUT); 
    pinMode(BIN1,OUTPUT);
  }
  myCmd = HC05.readStringUntil('\r');

  if(myCmd == "STRAIGHT"){ 
    digitalWrite(AIN2, HIGH);
    digitalWrite(BIN1, HIGH);
    analogWrite(pwm, 25);
  }
  if(myCmd == "RIGHT"){ 
    digitalWrite(AIN2, HIGH);
    digitalWrite(BIN1, LOW);
    analogWrite(pwm, 25);
  }
  if(myCmd == "LEFT"){ 
    digitalWrite(AIN2, LOW);
    digitalWrite(BIN1, HIGH);
    analogWrite(pwm, 25);
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
 