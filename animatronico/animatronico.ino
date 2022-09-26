#include <Servo.h>

int letraB, letraC, letraD, letraE, finalStr, NservoCabeza, NservoBrazoL, NservoBrazoD, NservoBicepL, NservoBicepD;
String datos, servoCabeza, servoBrazoL, servoBrazoD, servoBicepL, servoBicepD;

Servo servoMotorCabeza, servoMotorBrazoL, servoMotorBrazoD, servoMotorBicepL, servoMotorBicepD;

void setup() {
  Serial.begin(9600);
  servoMotorCabeza.attach(3);
  servoMotorBrazoL.attach(5);
  servoMotorBrazoD.attach(6);
  servoMotorBicepL.attach(9);
  servoMotorBicepD.attach(11);
}
void loop() {
  if(Serial.available() > 0){
    datos = Serial.readString();
    letraB = datos.indexOf('b');
    letraC = datos.indexOf('c');
    letraD = datos.indexOf('d');
    letraE = datos.indexOf('e');
    finalStr = datos.length();

    servoCabeza = datos.substring(1, letraB);
    servoBrazoL = datos.substring(letraB + 1, letraC);
    servoBrazoD = datos.substring(letraC + 1, letraD);
    servoBicepL = datos.substring(letraD + 1, letraE);
    servoBicepD = datos.substring(letraE + 1, finalStr);
  
    NservoCabeza = servoCabeza.toInt();
    NservoBrazoL = servoBrazoL.toInt();
    NservoBrazoD = servoBrazoD.toInt();
    NservoBicepL = servoBicepL.toInt();
    NservoBicepD = servoBicepD.toInt();

    //Serial.println(letraB);
    Serial.println(NservoCabeza);
    Serial.println(NservoBrazoL);
    Serial.println(NservoBrazoD);
    Serial.println(NservoBicepL);
    Serial.println(NservoBicepD);

    servoMotorCabeza.write(NservoCabeza);
    servoMotorBrazoL.write(NservoBrazoL);
    servoMotorBrazoD.write(NservoBrazoD);
    servoMotorBicepL.write(NservoBicepL);
    servoMotorBicepD.write(NservoBicepD);
  }
}
