#include <SoftwareSerial.h>
SoftwareSerial HC05(11,12); //Bluetooth connection

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
int pwm;
int pwmVal;
String myCmd;

void setup() {
  HC05.begin(9600);

  Serial.println("Enter command: ");
}
 
void loop() {
  if(HC05.available()){
    myCmd = HC05.readStringUntil('\r');
    Serial.println("You typed: ");
    Serial.println(myCmd);
  }
  //   //setMotor(myCmd, 25, PWM, AIN2, BIN1);
  //   if(myCmd.equals("straight")){ //STRAIGHT
  //         digitalWrite(AIN2, HIGH);
  //         digitalWrite(BIN1, HIGH);
  //     }
  //   else if(myCmd.equals("right")){ //LEFT
  //       digitalWrite(AIN2, HIGH);
  //       digitalWrite(BIN1, LOW);
  //     }
  //   else if(myCmd.equals("left")){ //RIGHT
  //       digitalWrite(AIN2, LOW);
  //       digitalWrite(BIN1, HIGH);   
  //     } 
  // }

}

// void readEncoder(){
//   int b = digitalRead(ENCB1);
//   if(b > 0){
//     pos++;
//   }
//   else{
//     pos--;
//   }
// }
 
// void setMotor(String myCmd, int pwmVal, int pwm, int in1, int in2){
    
//     analogWrite(pwm,pwmVal);

//     if(myCmd.equals("straight")){ //STRAIGHT
//       digitalWrite(in1, HIGH);
//       digitalWrite(in2, HIGH);
//     }
//     if(myCmd.equals("right")){ //LEFT
//       digitalWrite(in1, HIGH);
//       digitalWrite(in2, LOW);
//     }
//     if(myCmd.equals("left")){ //RIGHT
//       digitalWrite(in1, LOW);
//       digitalWrite(in2, HIGH);
//     }  
  
// }
 