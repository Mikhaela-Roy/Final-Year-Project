#include <SoftwareSerial.h>
SoftwareSerial HC05(11,12);

#define ENCA1 2
#define ENCA2 7
#define ENCB1 4
#define ENCB2 2
#define PWM 5
#define AIN2 5
#define AIN1 10
#define BIN2 9
#define BIN1 6
 
int pos = 0;
int myCmd;
 
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

  setMotor(1, 25, PWM, AIN2, BIN1);
  delay(200);
}
 
void setMotor(int myCmd, int pwmVal, int pwm, int in1, int in2){
  analogWrite(pwm,pwmVal);
  if(myCmd == 1){
    digitalWrite(in1,HIGH);
    digitalWrite(in2,LOW);
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