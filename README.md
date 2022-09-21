# El Charrito Electronico

Aqui se presenta el repositorio del proyecto del animatronico para el Cocotron 2022, realizado por el Laboratorio de Innovacion BUAP-Intel 
____

# Contenido

[Overview](#overview)  
[Miembros del Equipo](#miembros-del-equipo)  
[Leyenda "El Charro Negro"](#leyenda-el-charro-negro)  
[Desarrollo de la aplicacion](#desarrollo-de-la-aplicacion)  
[Evidencias](#evidencias)  
<a name="headers"/>
____

## Overview
Se desarrollo un aplicacion de escritorio en Python, que usa la camara para estimar la pose de la persona que esta siendo grabada, 
los datos de la estimacion son procesados y enviados a un microcontrolador para mover los servomotores del animatronico, de esta forma se logra que el robot 
imite los movimientos de una persona.
____
     
## Miembros del Equipo
Miembos del Laboratorio de Innovacion Intel-BUAP

|           Nombre              | Carrera         |  Semestre    |
|------------------------------ | ----------------|---------------
|Christian Rodriguez Hernandez  | Mecatronica     |     9°       |
|Marco  | Mecatronica     |     9°       |
|Rene  | Electronica     |     9°       |
|Adiel  | Electronica     |     9°       |
____

## Leyenda "El Charro Negro"

![charro](https://user-images.githubusercontent.com/85959332/191128216-8168bf73-f4b9-4af3-9dc5-f9ff2873f77d.png)

_El Charro provenía de una familia humilde. Sus padres, aunque lo amaban, nunca pudieron cumplirle sus caprichos. Al Charro siempre le gustó ir bien vestido, a veces incluso, no comía durante días para ahorrarse unos pesos y con lo juntado, poder completar para un buen sombrero._

_Sin embargo, estaba cansado de su inagotable pobreza. Por más que trabajaba, el dinero nunca le alcanzaba y tenía que andar todo el día con las manos llenas de tierra._

_Tiempo después, murieron sus padres. Al quedar solo, la miseria del Charro aumentó considerablemente por lo que tomó una decisión que cambiaría su vida: invocar al diablo para pedirle riqueza._

_No se sabe cómo lo consiguió, pero finalmente, Lucifer se apareció. Aquella entidad supo leer los ojos y el espíritu del hombre que lo había llamado, así que de inmediato le ofreció cantidades de dinero que ni siquiera en dos vidas podría gastar. Lo único que pedía a cambio, era su alma._

_El Charro, en ese entonces era altivo y valiente así que la Estrella de la Mañana no había logrado asustarlo y aceptó._

_Pasó el tiempo y poco a poco la juventud del Charro comenzó a despedirse. De repente, se dio cuenta de que estaba cansado de gastar sus riquezas en mujeres, apuestas, vino y costosos trajes. A la par, la sensación de soledad le oprimía el pecho y apenas lo dejaba respirar. Nadie lo quería por lo que era sino por las riquezas que poseía._

_El Charro ya se había olvidado de aquel trato que lo maldijo. Por eso, cuando se le apareció el diablo para recordarle que la hora del cobro estaba cerca, se asustó como nunca._

_El terror invadió a nuestro protagonista hasta el último rincón de sus entrañas. Recordó su deuda y, por cobardía, comenzó a ocultarse. Mandó al personal de su hacienda a poner cruces por toda su propiedad y a construir una pequeña capilla._

![charro2](https://user-images.githubusercontent.com/85959332/191129567-df92f352-24f9-4221-8ecc-106071aa0f96.png)

_No obstante, el recuerdo de la deuda pendiente no lo dejaba dormir ni disfrutar de los pocos meses que le quedaban de vida. Así que, en un arranque de miedo tomó a su mejor caballo junto con una bolsa que contenía unas cuantas monedas de oro que no se había gastado. Emprendió el viaje durante la noche, para que nadie lo viera huir._

_Sin embargo, el diablo se dio cuenta de que el Charro faltaría a su palabra así que volvió a aparecer frente al jinete y su caballo pero esta vez, con el fin de llevárselo._

_—Iba a esperar a que murieras para cobrar la deuda que tienes conmigo, pero, como te ocultas cobardemente, te llevaré ahora —dijo el diablo._

_El Charro no tuvo tiempo de responder. Cuando se dio cuenta, su caballo, encabritado, trató de patear al demonio pero era tarde, los brazos de su amo habían comenzado a secarse y su carne a desaparecer. Solo le quedaba el ajuar de Charro encima de los huesos blanquecinos. El diablo volvió a hablar:_

_—Veo que tu bestia te es fiel, por eso ha de ser maldita igual que tú y condenada a acompañarte a tu viaje hacia el infierno. Aunque, de vez en cuando, quiero que hagas algo por mí, cobrarle a mis deudores. Si haces bien tu trabajo, dejaré que el hombre que acepte esa bolsa con monedas de oro que traes, tome tu lugar._

_Desde entonces, aquel hombre fue condenado a sufrir incontables tormentos en el infierno y a salir de ahí solo para cobrar a quienes tienen deudas pendientes con Lucifer. Esto con la esperanza de que una noche, algún viajero, traicionado por su avaricia, tomé su lugar. Solo así, el Charro Negro y su caballo podrán descansar en paz._

Lyenda tomada de: Cisneros, S. (2022, January 28). La leyenda del Charro Negro. México Desconocido. Retrieved September 20, 2022, de [La Leyenda del Charrro Negro](https://www.mexicodesconocido.com.mx/la-leyenda-del-charro-negro.html)
____

## Desarrollo de la aplicacion
La aplicacion fue desarrollada en Python con los siguientes modulos:

```python
import numpy
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import *
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
____

## Evidencias
![Evidencia1](https://user-images.githubusercontent.com/85959332/191079474-2e9e440d-6382-4ff6-ba26-5d29fe0b017b.jpg)
> Trabajando en el Laboratorio de Innovacion de Intel, ubicado en el Edificio EMA7 salon 205.

![Qt Designer 19_09_2022 12_50_47 p  m](https://user-images.githubusercontent.com/85959332/191081543-f181fedd-51fe-49eb-ba49-695e9d3d2f43.png)
> Diseño de la interfaz grafica en Qt Designer.

![servo](https://user-images.githubusercontent.com/85959332/191537964-e1dc9e72-e472-43aa-aa1d-9807bcfc993b.jpg)
> Realizando pruebas con un servomotor

