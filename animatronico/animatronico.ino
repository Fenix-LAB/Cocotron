// Se incluye la libreria de servo
#include <ESP32Servo.h>

// Declaracion de variables
int letraA, letraB, letraC, letraD, letraE, letraF, letraG, finalStr, NservoCabeza, NservoBrazoL, NservoBrazoD, NservoBicepL, NservoBicepD, NservoPiernaL, NservoPiernaD;
String datos, servoCabeza, servoBrazoL, servoBrazoD, servoBicepL, servoBicepD, servoPiernaL, servoPiernaD;

// Objeto de la clase Servo para cada servomotor
Servo servoMotorCabeza, servoMotorBrazoL, servoMotorBrazoD, servoMotorBicepL, servoMotorBicepD, servoMotorPiernaL, servoMotorPiernaD;

void setup() {
  // Se inicia la comunicacion Serial
  Serial.begin(9600);          
  // Se definen los pines de los servomotores
  servoMotorCabeza.attach(23);
  servoMotorBrazoL.attach(22);
  servoMotorBrazoD.attach(13);
  servoMotorBicepL.attach(12);
  servoMotorBicepD.attach(21);
  servoMotorPiernaL.attach(19);
  servoMotorPiernaD.attach(18);
}
void loop() {
  // Se estara validadndo si existen datos seriales para leer
  if(Serial.available() > 0){
    // Los datos se guardan en la variable datos
    datos = Serial.readString();
    // Se obtiene la ubicacion de las letras que vienen en los datos
    letraA = datos.indexOf('a');
    letraB = datos.indexOf('b');
    letraC = datos.indexOf('c');
    letraD = datos.indexOf('d');
    letraE = datos.indexOf('e');
    letraF = datos.indexOf('f');
    letraG = datos.indexOf('g');
    finalStr = datos.length();   // Longitud de los datos para conocer la ubicacion del ultimo dato

    // Se obtienen los subdatos apartir de la ubicacion de las letras
    servoCabeza = datos.substring(letraA + 1, letraB);
    servoBrazoL = datos.substring(letraB + 1, letraC);
    servoBrazoD = datos.substring(letraC + 1, letraD);
    servoBicepL = datos.substring(letraD + 1, letraE);
    servoBicepD = datos.substring(letraE + 1, letraF);
    servoPiernaL = datos.substring(letraF + 1, letraG);
    servoPiernaD = datos.substring(letraG + 1, finalStr);

    // Se cambia el tipo de dato de String a entero
    NservoCabeza = servoCabeza.toInt();
    NservoBrazoL = servoBrazoL.toInt();
    NservoBrazoD = servoBrazoD.toInt();
    NservoBicepL = servoBicepL.toInt();
    NservoBicepD = servoBicepD.toInt();
    NservoPiernaL = servoPiernaL.toInt();
    NservoPiernaD  = servoPiernaD.toInt();
    
    // Los datos enteros son los angulos y estos se envian a los servomotores
    servoMotorCabeza.write(NservoCabeza);
    servoMotorBrazoL.write(NservoBrazoL);
    servoMotorBrazoD.write(NservoBrazoD);
    servoMotorBicepL.write(NservoBicepL);
    servoMotorBicepD.write(NservoBicepD);
    servoMotorPiernaL.write(NservoPiernaL);
    servoMotorPiernaD.write(NservoPiernaD);
  }
}
