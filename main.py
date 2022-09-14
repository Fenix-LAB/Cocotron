import numpy
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import *
from gui_design import *
from PyQt5.QtGui import *
import cv2
import mediapipe as mp
import imutils
from scipy.spatial import distance


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # Usamos la funcion QPoint() para guardar la posicion del mouse
        self.click_position = QPoint()
        # Se configura la ventana
        self.btn_normal.hide()
        self.btn_min.clicked.connect(lambda: self.showMinimized())
        self.btn_cerrar.clicked.connect(self.control_btn_cerrar)
        self.btn_normal.clicked.connect(self.control_btn_normal)
        self.btn_max.clicked.connect(self.control_btn_maximizar)
        self.btn_iniciar.clicked.connect(self.control_btn_iniciar)
        self.btn_detener.clicked.connect(self.control_btn_detener)
        self.btn_menu.clicked.connect(self.mover_menu)

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

        self.read_ports()
        self.start_video()
        self.data_control = False

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

    def control_btn_cerrar(self):
        self.close()
        # cap.release()
        self.label.clear()

    def control_btn_normal(self):
        self.showNormal()
        self.btn_normal.hide()
        self.btn_max.show()

    def control_btn_maximizar(self):
        self.showMaximized()
        self.btn_max.hide()
        self.btn_normal.show()

    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    def mousePressEvent(self, event):
        self.click_posicion = event.globalPos()

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
        self.comboBox_velocidad.setCurrentText("9600")

    def serial_conect(self):
        self.serial.waitForReadyRead(100)
        self.port = self.comboBox_puerto.currentText()
        self.baud = self.comboBox_velocidad.currentText()
        self.serial.setBaudRate(int(self.baud))
        self.serial.setPortName(self.port)
        self.serial.open(QIODevice.ReadWrite)

    def read_data(self):
        if not self.serial.canReadLine(): return
        rx = self.serial.readLine()

        datos = str(rx, 'utf-8').strip()

    def send_data(self, data):
        data = data + "\n"
        #print(data)
        if self.serial.isOpen():
            self.serial.write(data.encode())
            print("enviado")

    def control_btn_iniciar(self):
        self.Work.signalData.connect(self.detection_data)

    def control_btn_detener(self):
        self.data_control = False

    def start_video(self):
        self.Work = Work()
        self.Work.start()
        self.Work.Imageupd.connect(self.Imageupd_slot)

    def Imageupd_slot(self, Image):
        self.label_videocapture.setPixmap(QPixmap.fromImage(Image))

    def detection_data(self, data):
        self.data_control = True
        if self.data_control == True:
            self.send_data(str(data))
            #print(data)

class Work(QThread):
    Imageupd = pyqtSignal(QImage)
    signalData = pyqtSignal(int)

    def __init__(self, parent=None, index=0):
        super(Work, self).__init__(parent)
        self.index = index
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_holistic = mp.solutions.holistic
        self.mp_hands = mp.solutions.hands
        self.mp_pose = mp.solutions.pose

    def run(self):
        self.hilo_corriendo = True
        cap = cv2.VideoCapture(0)
        with self.mp_holistic.Holistic(
            static_image_mode=False,
            model_complexity=1,
            enable_segmentation=False,
        ) as holistic:
            while self.hilo_corriendo:
                ret, frame = cap.read()
                if ret:
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    results = holistic.process(frame_rgb)
                    # Mano izquieda
                    self.mp_drawing.draw_landmarks(
                        frame, results.left_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS,
                        self.mp_drawing.DrawingSpec(color=(255, 140, 0), thickness=2, circle_radius=1),
                        self.mp_drawing.DrawingSpec(color=(255, 255, 0), thickness=2))

                    # Mano derecha
                    self.mp_drawing.draw_landmarks(
                        frame, results.right_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS,
                        self.mp_drawing.DrawingSpec(color=(255, 140, 0), thickness=2, circle_radius=1),
                        self.mp_drawing.DrawingSpec(color=(255, 255, 0), thickness=2))

                    # Postura
                    self.mp_drawing.draw_landmarks(
                        frame, results.pose_landmarks, self.mp_holistic.POSE_CONNECTIONS,
                        self.mp_drawing.DrawingSpec(color=(255, 140, 0), thickness=2, circle_radius=1),
                        self.mp_drawing.DrawingSpec(color=(255, 255, 0), thickness=2))

                    Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    flip = cv2.flip(Image, 1)
                    frameu = imutils.resize(flip, width=640, height=480)
                    pic = QImage(frameu.data, frameu.shape[1], frameu.shape[0], QImage.Format_RGB888)
                    # pic = convertir_QT.scaled(320, 240, Qt.KeepAspectRatio)
                    self.Imageupd.emit(pic)
                    lmList = []
                    h, w, c = frame.shape
                    if results.pose_landmarks:
                        for id, lm in enumerate(results.pose_landmarks.landmark):
                            # print(id, lm)
                            cx, cy, cz = int(lm.x * w), int(lm.y * h), int(lm.z * c)
                            lmList.append([id, cx, cy, cz])

                        if lmList:
                            head = self.headDet(lmList)

                            self.signalData.emit(head)

    def headDet(self, lmList):
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

    def headDirection(self, LI, LD):
        if LI > LD + 20:
            return 1 #Lado derecho
        elif LD > LI + 20:
            return 2 #Lado izquierdo
        else:
            return 0 #Centro

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyApp()
    window.show()
    app.exec_()
