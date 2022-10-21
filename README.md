# El Charrito Electronico

Aqui se presenta el repositorio del proyecto del animatronico para el Cocotron 2022, realizado por el Laboratorio de Innovacion BUAP-Intel 
____

## Contenido

[Overview](#overview)  
[Miembros del Equipo](#miembros-del-equipo)  
[Leyenda "El Charro Negro"](#leyenda-el-charro-negro)          
[Antecedentes](#antecedentes)     
[Desarrollo de la aplicacion](#desarrollo-de-la-aplicacion)  
[Codigo en Arduino](#codigo-en-arduino)      
[Evidencias](#evidencias)  
<a name="headers"/>
____

## Overview
Se desarrollo una aplicacion de escritorio en Python, que usa la camara para estimar la pose de la persona que esta siendo grabada, 
los datos de la estimacion son procesados y enviados a un microcontrolador para mover los servomotores del animatronico, de esta forma se logra que el robot 
imite los movimientos de una persona.
____
     
## Miembros del Equipo
Miembos del Laboratorio de Innovacion Intel-BUAP

|           Nombre              | Carrera         |  Semestre    |
|------------------------------ | ----------------|---------------
|Christian Rodriguez Hernandez  | Mecatronica     |     9°       |
|Marco Antonio Ruiz Guagnelli | Mecatronica     |     9°       |
|Maria Fernanda Hernandez Ramos  | Electronica     |     9°       |
|Adiel Sanchez Santos  | Electronica     |     9°       |
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

## Antecedentes

En México, la leyenda del charro negro tiene dos historias distintas según la zona donde se esté relatando, estas áreas se encuentran en el área del centro y sureste de México ( Puebla, CDMX , Veracruz, Hidalgo, etc.) y la otra en la zona oeste y suroeste de México ( Guadalajara, Aguascalientes, etc.), pero nosotros nos enfocamos en la versión de nuestro estado.

Los antecedentes de esta leyenda no son certeros, pero se piensa que se originó en alguno de los estados de Puebla, Tlaxcala, Veracruz e Hidalgo. 

Según algunos, la leyenda surge entre el **sincretismo** en el año 1920 entre creencias indígenas y europeas. El Charro Negro representa el lado oscuro del alma humana, una historia que advierte sobre la cegadora codicia. Este personaje fue transmutado en deidades oscuras por etnias como la **Wixárika**. Dentro de las deidades Huicholes, el que más resalta dentro de estas deidades es el dios Tamatsi Teiwari Yuawi, que en español es llamado "Nuestro Hermano Mayor el Mestizo Azul Oscuro". El dios "Mestizo Azul", dentro de la cultura indígena, específicamente dentro de la cultura Huichol, representa el estereotipo del colonizador que llega a amenazar su cultura. Este dios "Mestizo Azul" es más poderoso que los mismos dioses Huicholes, sin embargo, es déspota, cobrador y no conoce el perdón. El resultado del encuentro de estas dos culturas también une dos religiones; la mesoamericana (específicamente la Huichol) y de España, el resultado será una cultura popular Mestiza, que crea una figura del folclore mexicano, es decir el "Charro Negro".

Desde una perspectiva mixteca, se cuenta que es el "patrón del lugar" habita en la cima del monte, cuidador de la comarca, este individuo no tiene aspectos indígenas, al contrario, nos habla de características de los colonizadores, es decir un hombre blanco, alto y montado a caballo. Los Mixtecos hablan de lo peligroso que puede ser encontrarlo, por eso se tiene la creencia de cargar ajo, para lograr ahuyentarlo. Este "señor del cerro" castiga a los que causan destrozos en los bosques, custodia los tesoros y castiga a quienes cometen avaricia. Tal es la importancia del "Señor del Cerro" que los indígenas pedían permiso con ofrendas para poder obtener el permiso de trabajar en sus tierras. Las ofrendas constaban de cigarro, mezcal y comida.

En la Sierra Norte de Puebla, San Martín de Caballero, es conocido en las ciudades como un santo al cuál se le pide dinero con la frase "San Martín de Caballero, dame tantito dinero" mientras se le ofrece alfalfa a su caballo. Mientras que en la cultura Mazatecos se convierte en un ser nocturno, en donde explican que no se trata de un santo. Se le conoce como el dueño de las tierras y de los montes. Sus características son de colonizadores, es de tez blanca y saluda en castellano. Algunas noches baja para visitar a sus animales y vigilar los tesoros enterrados. Los que desean obtener dinero de este ser, deben de ir en estado de indulgencia (abstinencia sexual) y llegan ofreciendo cacao o un guajolote. San Martín de Caballero, les da instrucciones, en las que se incluye, llevarse su caballo de la cola hasta la casa del solicitante y no decir nada en 4 años, si esta promesa se llega a romper entonces queda condena el alma del solicitante, muere al instante y San Martín de Caballero toma su cuerpo y alma para llevarlos a trabajar con él.

Con la llegada del cristianismo a México, la dualidad también se propulsó con la figura de Dios y Lucifer, y en esta bifurcación cultural surgieron mitos y leyendas sobre la tentación perenne que es capaz de hacer perecer el alma.
____

## Desarrollo de la aplicacion
La aplicacion fue desarrollada en Python con los siguientes modulos:

```python
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
import mediapipe as mp
import imutils
from scipy.spatial import distance
```
#### PyQt5
Este modulo es una clase que nos permite crear interfaces graficas, tiene una coleccion de metodos y eventos para la realizacion de la aplicacion.
Este modulo tambien incluye submodulos muy importantes, como el QtSerialPort para la comunicacion serial con el microcontrolador, o QThread para usar el multihilo del procesador.

#### MediaPipe
MediaPipe ofrece soluciones de Machine Learning personalizables y multiplataforma para medios en vivo y de transmisión.
Es el modulo encargado de estimar la pose de las personas.

#### OpenCV
Modulo muy popular de Computer Vision que permite usar algoritmos de Machine Learning en videos o imagenes. 
Fue utilizado para procesar el video.

### Clases de la aplicacion
La aplicacion consta de dos clases, la primera es la clase de la ventana donde se encuentran los metodos de los botones, de mostrar la imagen y enviar los datos de forma Serial.
En la otra clase se realiza el procesamiento de las imagenes para estimar la pose de las personas, en esta clase tambien se calculan
los angulos de los movimientos de las personas, esta es la informacion que se envia por comunicacion Serial.
#### Clase MyApp()
Para la clase de la ventana se crearon los siguientes metodos:
```python
mover_menu(self): 
control_btn_cerrar(self):
control_btn_normal(self):
control_btn_maximizar(self):
resizeEvent(self, event):
mousePressEvent(self, event):
mover_ventana(self, event):
read_ports(self):
serial_conect(self):
read_data(self):
send_data(self, data):
control_btn_iniciar(self):
control_btn_detener(self):
start_video(self):
Imageupd_slot(self, Image):
detection_data(self, data):
```

#### Clase Work()
En la clase de Work se hizo heredandola de la clase QThread para usar el multinucleo del procesador
```python
class Work(QThread):
```

En esta clase se definen dos variables qus son señales que despues seran usadas por la clase de la ventana
```python
Imageupd = pyqtSignal(QImage)     # Variable de tipo señal para guardar la imagen mostrada
signalData = pyqtSignal(str)      # Variable de tipo señal para gairdar lso datos que se enviaran
```

En el metodo de Run se realiza el procesado del video, la estimacion de pose y el procesado de los angulos de las partes del cuerpo

- Para el procesado del video se usan las funciones de CV2 como:
```python
VideoCapture()
read()
cvtColor()
flip() 
```

- Para la estimacion de pose se usan las siguientes funciones de mediapipe
```python
Holistic()
process()
draw_landmarks()
```

- Los puntos de la estimacion de pose se guardan en:
```python
lmList
```

- Con los puntos de la estimacion de pose se calculan los angulos y se hace el String que sera enviado por comunicacion Serial
```python
data = 'a' + str(head) + 'b' + str(brazoL) + 'c' + str(brazoD) + 'd' +\
                        str(bicepL) + 'e' + str(bicepD) + 'f' + str(piernaL) + 'g' + str(piernaD)
```
____

## Codigo en Arduino
La unica libreria que se agrego fue la siguiente:

```c++
#include <ESP32Servo.h>
```

El codigo revisa si existen datos en el puerto serial y cuando llegan los datos los guarda en una variable de tipo String,
los datos que se reciben son de la siguiente forma:

```c++
'a' + "Angulo de la cabeza" + 'b' + "Brazo izquierdo" + 'c' + "Brazo derecho" + 'd' + "Bicep izquierdo" + 'e' + "Bicep derecho" + 'f' + "Pierna izquierda" + 'g' + "Pierna derecha"
```

Por ejemplo:

```c++
a90b30c30d170e170f90g90
```

El programa realiza las siguientes aperaciones:
- Guardar el String en la variable "datos"
- Ubicar la posicion de la las letras a, b, c, d, e y ubicacion del ultimo caracter
- Obtener el subString donde se encuentra el valor de los angulos
- Convertir los angulos de String a Entero
- Los angulos se limitan entre 0 y 180
- Angunos angulos son cambiados de 0-180 a 180-0
- Enviar el angulo a los servomotores

A lo largo del codigo se usaron las siguientes funciones:

```c++
readString() // Leer datos seriales
indexOf()    // Posicion de un caracter esoecificado
substring()  // Obtener un subString
toInt()      // Convertir String a Entero
write()      // Enviar posicion de servomotor
```
____

## Evidencias
![Evidencia1](https://user-images.githubusercontent.com/85959332/191079474-2e9e440d-6382-4ff6-ba26-5d29fe0b017b.jpg)
> Trabajando en el Laboratorio de Innovacion de Intel, ubicado en el Edificio EMA7 salon 205.

![Qt Designer 19_09_2022 12_50_47 p  m](https://user-images.githubusercontent.com/85959332/191081543-f181fedd-51fe-49eb-ba49-695e9d3d2f43.png)
> Diseño de la interfaz grafica en Qt Designer.

![animatronico Arduino 1 8 19 21_09_2022 12_54_38 p  m](https://user-images.githubusercontent.com/85959332/191576390-45c51f22-9c93-4193-bac4-c9d490b6d620.png)
> Trabajando en el codigo en Arduino IDE.

![servo](https://user-images.githubusercontent.com/85959332/191537964-e1dc9e72-e472-43aa-aa1d-9807bcfc993b.jpg)
> Realizando pruebas con un servomotor.

![2](https://user-images.githubusercontent.com/85959332/192871657-458ce2be-c3ce-4214-8897-980473b7720c.jpg)
> Conexion de 7 servomotores.

![3](https://user-images.githubusercontent.com/85959332/192871672-6e3612b2-6de5-44b3-8356-f9b6e7df443d.jpg)
> Test de la aplicacion en conjunto con los servomotores.

![solidasm](https://user-images.githubusercontent.com/85959332/195206752-2db37341-a5a0-453f-9019-9d352307cc5b.jpg)
> Ensamble en SolidWorks.

![3d2](https://user-images.githubusercontent.com/85959332/194435481-0e98be57-5192-42f7-a49b-c350478e4ab0.jpg)
> Impresion de piezas en impresora 3D.

![3d1](https://user-images.githubusercontent.com/85959332/194435488-efdf3443-6b8c-4346-a008-12ebdedf898c.jpg)
> Impresion de piezas en impresora 3D.

![pint_hacienda](https://user-images.githubusercontent.com/85959332/196570927-60e31f16-139c-456d-ac3a-d1008c994777.jpg)
> Trabajando en la hacienda.

![escenario](https://user-images.githubusercontent.com/85959332/196522230-40f8af58-522d-4cf8-8b10-e739d2292828.jpg)
> Realizando el escenario.

![ad](https://user-images.githubusercontent.com/85959332/197199389-1f0db63a-043c-4f1c-9681-94a2521b81be.jpg)
> Realizando el escenario.

![trabajando](https://user-images.githubusercontent.com/85959332/196570949-a43fa0a4-ded0-404a-8d56-7df52fd57e62.jpg)
> Realizando el escenario.

![armado](https://user-images.githubusercontent.com/85959332/196522257-9f253250-1d10-4195-aa34-67cf0b46ecac.jpg)
> Armando el robot.

![charro](https://user-images.githubusercontent.com/85959332/197044820-6f5a504a-8049-486c-ac1b-23f43759e48b.jpg)
> Charrito.

![charro_luz](https://user-images.githubusercontent.com/85959332/197044778-5d22ce42-a725-459c-8b2f-33dc207f98a7.jpg)
> Charro con luz.



