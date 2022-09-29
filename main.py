# Importacion de las librerias
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo   # Modulo Serial de PyQt5
from PyQt5.QtCore import *                                    # Modulo PyQt5 para intarfaces graficas
from gui_design import *
from PyQt5.QtGui import *
import cv2                                                    # CV2 para la creacion del video
import mediapipe as mp                                        # Modulo para la estimacion de pose
import imutils
import math
from scipy.spatial import distance

#Clase de la ventana heredada de la interfaz "gui_design.py"
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    # Se define le contructor con todos los atributos necesarios y asociacion de metodos
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # Usamos la funcion QPoint() para guardar la posicion del mouse
        self.click_position = QPoint()
        self.btn_menu.clicked.connect(self.mover_menu)

        # Se configura la ventana asociando los eventos con metodos
        self.btn_normal.hide()
        self.btn_min.clicked.connect(lambda: self.showMinimized())
        self.btn_cerrar.clicked.connect(self.control_btn_cerrar)
        self.btn_normal.clicked.connect(self.control_btn_normal)
        self.btn_max.clicked.connect(self.control_btn_maximizar)
        self.btn_iniciar.clicked.connect(self.control_btn_iniciar)
        self.btn_detener.clicked.connect(self.control_btn_detener)

        # Se elimina la barra de titulo por default
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Size grip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # Movimiento de la ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana

        # Control connect
        self.serial = QSerialPort()
        self.btn_actualizar.clicked.connect(self.read_ports)
        self.btn_conectar.clicked.connect(self.serial_conect)
        self.btn_desconectar.clicked.connect(lambda: self.serial.close())

        # Asociacion de metodos
        self.serial.readyRead.connect(self.read_data)

        # Se inician los siguientes metodos y atributos adicionles
        self.read_ports()
        self.start_video()
        self.data_control = False

    # Metodo del boton de menu
    def mover_menu(self):
        if True:
            width = self.frame_menu.width()
            normal = 0
            if width == 0:
                extender = 250
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.frame_menu, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()

    # Metodo del boton cerrar
    def control_btn_cerrar(self):
        self.close()
        # cap.release()
        self.label.clear()

    # Metodo del boton de ventana normal
    def control_btn_normal(self):
        self.showNormal()
        self.btn_normal.hide()
        self.btn_max.show()

    # Metodo del boton de minimizar
    def control_btn_maximizar(self):
        self.showMaximized()
        self.btn_max.hide()
        self.btn_normal.show()

    # Metodo para redimensionar la ventana
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    def mousePressEvent(self, event):
        self.click_posicion = event.globalPos()

    # Metodo para mover la ventana por la barra de titulo
    def mover_ventana(self, event):
        if self.isMaximized() == False:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.click_posicion)
                self.click_posicion = event.globalPos()
                event.accept()
        if event.globalPos().y() <= 5 or event.globalPos().x() <= 5:
            self.showMaximized()
            self.btn_max.hide()
            self.btn_normal.show()
        else:
            self.showNormal()
            self.btn_normal.hide()
            self.btn_max.show()

    # Metodo para leer los puertos y seleccionar la velocidad de los datos
    def read_ports(self):
        self.baudrates = ['1200', '2400', '4800', '9600', '19200', '34800', '115200']
        portList = []
        ports = QSerialPortInfo().availablePorts()
        for i in ports:
            portList.append(i.portName())

        self.comboBox_puerto.clear()
        self.comboBox_velocidad.clear()
        self.comboBox_puerto.addItems(portList)
        self.comboBox_velocidad.addItems(self.baudrates)
        self.comboBox_velocidad.setCurrentText("9600")      # Se coloca por default una velocidad de  9600 baudios

    # Conexion con las caracteristicas especificadas de velocidad y puerto
    def serial_conect(self):
        self.serial.waitForReadyRead(100)
        self.port = self.comboBox_puerto.currentText()
        self.baud = self.comboBox_velocidad.currentText()
        self.serial.setBaudRate(int(self.baud))
        self.serial.setPortName(self.port)
        self.serial.open(QIODevice.ReadWrite)

    # Metodo para leer datos seriales (No se uso en esta aplicacion)
    def read_data(self):
        if not self.serial.canReadLine(): return
        rx = self.serial.readLine()

        datos = str(rx, 'utf-8').strip()

    # Metodo para enviar datos por comunicacion Serial
    def send_data(self, data):
        data = data + "\n"
        #data = data
        #print(data)
        if self.serial.isOpen():
            self.serial.write(data.encode())
            #print("enviado")

    # El boton para iniciar el envio de datos
    def control_btn_iniciar(self):
        self.Work.signalData.connect(self.detection_data) # Se enlaza el atributo de datos con el metodo para enviarlos

    # Boton para detener el envio de datos
    def control_btn_detener(self):
        self.data_control = False

    # Metodo que inicia el video (Este metodo es llamado al inicio)
    def start_video(self):
        self.Work = Work()
        self.Work.start()
        self.Work.Imageupd.connect(self.Imageupd_slot) # Se enlaza el atributo de imagen con el metodo que la mostrara

    # Metodo que envia cada frame a la interfaz
    def Imageupd_slot(self, Image):
        self.label_videocapture.setPixmap(QPixmap.fromImage(Image))

    # Se envian los datos de la estimacion de pose por comunicacion Serial
    def detection_data(self, data):
        self.data_control = True
        if self.data_control == True:
            self.send_data(str(data))
            #print(data)

# Clase auxiliar, heredada de QThread para poder usar el multinucleo y tener un mejor video
class Work(QThread):
    Imageupd = pyqtSignal(QImage)     # Variable de tipo señal para guardar la imagen mostrada
    signalData = pyqtSignal(str)      # Variable de tipo señal para guardar lso datos que se enviaran

    # Se define el contructor de la clase
    def __init__(self, parent=None, index=0):  # Por default se inicia en el nucleo 0
        super(Work, self).__init__(parent)
        self.index = index
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_holistic = mp.solutions.holistic
        self.mp_hands = mp.solutions.hands
        self.mp_pose = mp.solutions.pose

    # Metodo donde se procesa el video
    def run(self):
        self.hilo_corriendo = True
        cap = cv2.VideoCapture(0)     # Se define que se leera una camara del dispositivo
        s=0
        with self.mp_holistic.Holistic(    #Atributos de la estimacion de pose
            static_image_mode=False,
            model_complexity=1,
            enable_segmentation=False,
        ) as holistic:
            while self.hilo_corriendo:    # Ciclo que estara permanentemente recibiendo imagenes de la camara
                ret, frame = cap.read()
                s += 1
                if ret:
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Se cambia el formatod de BGR a RGB
                    results = holistic.process(frame_rgb)
                    # Mano izquieda
                    #self.mp_drawing.draw_landmarks(                     # Se estima la pose de la mano izquierda
                        #frame, results.left_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS,
                        #self.mp_drawing.DrawingSpec(color=(255, 140, 0), thickness=2, circle_radius=1),
                        #self.mp_drawing.DrawingSpec(color=(255, 255, 0), thickness=2))

                    # Mano derecha
                    #self.mp_drawing.draw_landmarks(                      # Se estima la pose de la mano derecha
                        #frame, results.right_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS,
                        #self.mp_drawing.DrawingSpec(color=(255, 140, 0), thickness=2, circle_radius=1),
                        #self.mp_drawing.DrawingSpec(color=(255, 255, 0), thickness=2))

                    # Postura
                    self.mp_drawing.draw_landmarks(                      # Se estima la pose del cuerpo completo
                        frame, results.pose_landmarks, self.mp_holistic.POSE_CONNECTIONS,
                        self.mp_drawing.DrawingSpec(color=(255, 140, 0), thickness=2, circle_radius=1),
                        self.mp_drawing.DrawingSpec(color=(255, 255, 0), thickness=2))

                    Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    flip = cv2.flip(Image, 1)                           # Se hace una rotaccion de la imagen
                    frameu = imutils.resize(flip, width=640, height=480)
                    pic = QImage(frameu.data, frameu.shape[1], frameu.shape[0], QImage.Format_RGB888)
                    # pic = convertir_QT.scaled(320, 240, Qt.KeepAspectRatio)
                    self.Imageupd.emit(pic)                             # La imagen es enviada a la variable señal

                    # Se obtienen la ubicacion de los puntos de la estimacion de pose
                    lmList = []
                    h, w, c = frame.shape
                    if results.pose_landmarks:
                        for id, lm in enumerate(results.pose_landmarks.landmark):
                            # print(id, lm)
                            cx, cy = int(lm.x * w), int(lm.y * h)
                            lmList.append([id, cx, cy])

                        if lmList:
                            #Se obtiene los angulos de algunos movimientos del cuerpo
                            head = int(self.cabezaDet(lmList))
                            brazoL = int(self.brazoLDet(lmList))
                            brazoD = int(self.brazoDDet(lmList))
                            bicepL = int(self.bicepIDet(lmList))
                            bicepD = int(self.bicepDDet(lmList))
                            piernaL = int(self.piernaLDet(lmList))
                            piernaD = int(self.piernaDDet(lmList))

                            # Se crea el String que sera enviado por comunicacion Serial
                            data = 'a' + str(head) + 'b' + str(brazoL) + 'c' + str(brazoD) + 'd' +\
                                   str(bicepL) + 'e' + str(bicepD) + 'f' + str(piernaL) + 'g' + str(piernaD)
                            if s == 20:
                                #print(data)
                                self.signalData.emit(data)   # Se envia el String a la variable señal
                                s = 0

    # Direccion de la cabeza
    def cabezaDet(self, lmList):
        # Giro Cabeza
        PCx = lmList[0][1]
        PCy = lmList[0][2]
        PCIx = lmList[7][1]
        PCIy = lmList[7][2]
        PCDx = lmList[8][1]
        PCDy = lmList[8][2]
        # Distancia a lado izquierdo
        a_LID = (PCx, PCy)
        b_LI = (PCIx, PCIy)
        CDLI = int(distance.euclidean(a_LID, b_LI))
        # print(CDLI)
        # Distancia lado derecho
        # a_LD = (PCx, PCy)
        b_LD = (PCDx, PCDy)
        CDLD = int(distance.euclidean(a_LID, b_LD))
        # print("LD", CDLD,"LI", CDLI)
        direct = self.headDirection(CDLI, CDLD)
        return direct

    # Calculo del angulo del brazo izquierdo
    def brazoLDet(self, lmList):
        BIx1 = lmList[11][1]
        BIy1 = lmList[11][2]
        BIx2 = lmList[13][1]
        BIy2 = lmList[13][2]
        BIx3 = lmList[15][1]
        BIy3 = lmList[15][2]
        angle = self.angleVectors(BIx1, BIy1, BIx2, BIy2, BIx3, BIy3)
        return angle

    # Calculo del angulo del brazo derecho
    def brazoDDet(self, lmList):
        BDx1 = lmList[16][1]
        BDy1 = lmList[16][2]
        BDx2 = lmList[14][1]
        BDy2 = lmList[14][2]
        BDx3 = lmList[12][1]
        BDy3 = lmList[12][2]
        angle = self.angleVectors(BDx1, BDy1, BDx2, BDy2, BDx3, BDy3)
        return angle

    # Calculo del angulo del bicep izquierdo
    def bicepIDet(self, lmList):
        BIx1b = lmList[13][1]
        BIy1b = lmList[13][2]
        BIx2b = lmList[11][1]
        BIy2b = lmList[11][2]
        BIx3b = lmList[23][1]
        BIy3b = lmList[23][2]
        angle = self.angleVectors(BIx1b, BIy1b, BIx2b, BIy2b, BIx3b, BIy3b)
        return  angle

    # Calculo del angulo del bicep derecho
    def bicepDDet(self, lmList):
        BDx1b = lmList[24][1]
        BDy1b = lmList[24][2]
        BDx2b = lmList[12][1]
        BDy2b = lmList[12][2]
        BDx3b = lmList[14][1]
        BDy3b = lmList[14][2]
        angle = self.angleVectors(BDx1b, BDy1b, BDx2b, BDy2b, BDx3b, BDy3b)
        return angle

    # Calculo del angulo de la pierna izquierda
    def piernaLDet(self, lmList):
        PIx1 = lmList[25][1]
        PIy1 = lmList[25][2]
        PIx2 = lmList[23][1]
        PIy2 = lmList[23][2]
        PIx3 = lmList[24][1]
        PIy3 = lmList[24][2]
        angle = self.angleVectors(PIx1, PIy1, PIx2, PIy2, PIx3, PIy3)
        return angle

    # Calculo del angulo de la pierna derecha
    def piernaDDet(self, lmList):
        PDx1 = lmList[23][1]
        PDy1 = lmList[23][2]
        PDx2 = lmList[24][1]
        PDy2 = lmList[24][2]
        PDx3 = lmList[26][1]
        PDy3 = lmList[26][2]
        angle = self.angleVectors(PDx1, PDy1, PDx2, PDy2, PDx3, PDy3)
        return angle

    # Funcion para calcular el angulo de los vectores
    def angleVectors(self, x1, y1, x2, y2, x3, y3):
        # Calculate the Angle
        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
        if angle < 0:
            angle += 360
        return angle

    # Funcion para determinar la ddireccion de la cabeza
    def headDirection(self, LI, LD):
        if LI > LD + 20:
            return 0 #Lado derecho
        elif LD > LI + 20:
            return 180 #Lado izquierdo
        else:
            return 90 #Centro

# Se ejecuta la clase de la ventana
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyApp()
    window.show()
    app.exec_()
