#include <Servo.h>

#define led 13
int datoNum;
String datos;

Servo servoMotor;

void setup() {
  Serial.begin(9600);
  servoMotor.attach(5);
  pinMode(led, OUTPUT);
}
void loop() {
  if(Serial.available() > 0){
    datos = Serial.readString();
  datoNum = datos.toInt();
  if(datoNum==0){
        servoMotor.write(90);
        //Serial.println(90);
        //digitalWrite(led, HIGH);
      }
  if(datoNum==1){
        servoMotor.write(0);
        //Serial.println(0);
      }
  if(datoNum==2){
        servoMotor.write(180);
        //Serial.println(180);
      }
  }
  delay(200);
  
}
