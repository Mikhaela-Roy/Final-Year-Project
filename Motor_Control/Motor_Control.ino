#define ENCA1 3 // pin3 of the Arduino
#define ENCA2 7 // Pin7 of the Arduino
#define ENCB1 4 // pin4 of the Arduino
#define ENCB2 2 // Pin2 of the Arduino
#define AIN1 10 //
#define AIN2 5  //
#define BIN1 6  //
#define BIN2 9  //
int ENCA1_DATA; //
int ENCA2_DATA; //
int ENCB1_DATA; //
int ENCB2_DATA; //

boolean buttonState = LOW;
int rotDirection = 0;
int pressed = false;
 
void setup() {
  Serial.begin(9600); // Activates Serial communication
  pinMode(ENCA1, OUTPUT); 
  pinMode(ENCA2, OUTPUT); 
  pinMode(ENCB1, OUTPUT); 
  pinMode(ENCB2, OUTPUT); 
  pinMode(AIN1, INPUT);
  pinMode(AIN2, INPUT);
  pinMode(BIN1, INPUT);
  pinMode(BIN2, INPUT);
  //SETTING INITIAL ROTATIONAL DIRECTION
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, HIGH);
  digitalWrite(BIN2, HIGH);
}
 
void loop() {
  int potValue = analogRead(A0);
  int pmwOutput = map(potValue, 0, 1023, 0, 255);
  analogWrite(AIN1, potValue);
  analogWrite(AIN2, potValue);
  analogWrite(BIN1, potValue);
  analogWrite(BIN2, potValue);
  IF (digitalRead(button) == true ){
    pressed != pressed;
  }
  while (digitalRead(button) == true){
    delay(20);
  }
  if (pressed == true & rotDirection == 0){
    digitalWrite(AIN1, HIGH);
    digitalWrite(AIN2, HIGH);
    digitalWrite(BIN1, LOW);
    digitalWrite(BIN2, LOW);
    rotDirection = 1;
    delay(20);
  }

  if(pressed == false & rotDirection == 1) {
    digitalWrite(AIN1, LOW);
    digitalWrite(AIN2, LOW);
    digitalWrite(BIN1, HIGH);
    digitalWrite(BIN2, HIGH;
  }
  ENCA1_DATA = digitalRead(ENCA1); 
  ENCA2_DATA = digitalRead(ENCA2); 
// We simply read Pin2 of the Arduino and store the result in variable ENCA_DATA
  ENCB1_DATA = digitalRead(ENCB1); 
  ENCB2_DATA = digitalRead(ENCB2); 
// We simply read Pin3 of the Arduino and store the result in variable b
  Serial.println("ENCODER 1: ");
  Serial.println(ENCA1_DATA*5);
  Serial.println("ENCODER 1: ");
  Serial.println(ENCA2_DATA*5); 
  Serial.println("ENCODER 2: ");
  Serial.println(ENCB1_DATA*5);
  Serial.println("Encoder 2: ");
  Serial.println(ENCB2_DATA*5); 
}