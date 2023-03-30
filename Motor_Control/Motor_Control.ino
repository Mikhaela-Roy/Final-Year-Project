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
 
void setup() {
  Serial.begin(9600);
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
  setMotor(1, 25, PWM, AIN1, AIN2);
  setMotor(1, 25, PWM, BIN1, BIN2);
  delay(200);
  Serial.println(pos);
  setMotor(-1, 25, PWM, AIN1, AIN2);
  setMotor(-1, 25, PWM, BIN1, BIN2);
  delay(200);
  Serial.println(pos);
  setMotor(0, 25, PWM, AIN1, AIN2);
  setMotor(0, 25, PWM, BIN1, BIN2);
  delay(20);
  Serial.println(pos);
}
 
void setMotor(int dir, int pwmVal, int pwm, int in1, int in2){
  analogWrite(pwm,pwmVal);
  if(dir == 1){
    digitalWrite(in1,HIGH);
    digitalWrite(in2,LOW);
  }
  else if(dir == -1){
    digitalWrite(in1,LOW);
    digitalWrite(in2,HIGH);
  }
  else{
    digitalWrite(in1,LOW);
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