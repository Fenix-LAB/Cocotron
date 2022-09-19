# El Charrito Electronico

Aqui se presenta el repositorio del proyecto del animatronico para el Cocotron 2022, realizado por el Laboratorio de Innovacion BUAP-Intel 

## Overview
Se desarrollo un aplicacion de escritorio en Python, que usa la camara para estimar la pose de la persona que esta siendo grabada, 
los datos de la estimacion son procesados y enviados a un microcontrolador para mover los servomotores del animatronico, de esta forma se logra que el robot 
imite los movimientos de una persona.

## Desarrollo de la aplicacion
La aplicacion fue desarrollada en Python con los siguientes modulos:

```sh
import numpy
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import *
from gui_design import *
from PyQt5.QtGui import *
import cv2
import mediapipe as mp
import imutils
from scipy.spatial import distance
```
#### PyQt5
Este modulo es una clase que nos permite crar interfaces graficas, tiene una coleccion de metodos y eventos para la realizacion de la aplicacion.
Este modulo tambien incluye submodulos muy importantes, como el QtSerialPort para la comunicacion serial con el microcontrolador, o QThread para usar el multihilo del procesador.

#### MediaPipe
MediaPipe ofrece soluciones de Machine Learning personalizables y multiplataforma para medios en vivo y de transmisión.
Es el modulo encargado de estimar la pose de las personas.

#### OpenCV
Modulo muy popular de Computer Vision que permite usar algoritmos de Machine Learning en videos o imagenes. 
Fue utilizado para procesar el video.

## Evidencias
Trabajando en el Laboratorio de Innovacion de Intel, ubicado en el Edificio EMA7 salon 205.
![Evidencia1](https://user-images.githubusercontent.com/85959332/191079474-2e9e440d-6382-4ff6-ba26-5d29fe0b017b.jpg)
Diseño de la interfaz grafica en Qt Designer.

