# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1348, 820)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(84,111,236);\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(3, 0, 3, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_superior = QtWidgets.QFrame(self.frame)
        self.frame_superior.setMinimumSize(QtCore.QSize(0, 48))
        self.frame_superior.setMaximumSize(QtCore.QSize(16777215, 48))
        self.frame_superior.setStyleSheet("QFrame{\n"
"background-color: rgb(84,111,236);\n"
"}\n"
"\n"
"QPushButton{\n"
"border-radius:18px;\n"
"background-color: rgb(84,111,236);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(39,74,233);\n"
"}")
        self.frame_superior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_superior)
        self.horizontalLayout_2.setContentsMargins(10, 0, 5, 0)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_menu = QtWidgets.QPushButton(self.frame_superior)
        self.btn_menu.setMinimumSize(QtCore.QSize(50, 36))
        self.btn_menu.setMaximumSize(QtCore.QSize(50, 36))
        self.btn_menu.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(39,74,233);\n"
"border-radius: 5px\n"
"}")
        self.btn_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QtCore.QSize(36, 36))
        self.btn_menu.setObjectName("btn_menu")
        self.horizontalLayout_2.addWidget(self.btn_menu)
        spacerItem = QtWidgets.QSpacerItem(844, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_min = QtWidgets.QPushButton(self.frame_superior)
        self.btn_min.setMinimumSize(QtCore.QSize(36, 36))
        self.btn_min.setMaximumSize(QtCore.QSize(36, 36))
        self.btn_min.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_min.setIcon(icon1)
        self.btn_min.setIconSize(QtCore.QSize(36, 36))
        self.btn_min.setObjectName("btn_min")
        self.horizontalLayout_2.addWidget(self.btn_min)
        self.btn_max = QtWidgets.QPushButton(self.frame_superior)
        self.btn_max.setMinimumSize(QtCore.QSize(36, 36))
        self.btn_max.setMaximumSize(QtCore.QSize(36, 36))
        self.btn_max.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/chevrons-up.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_max.setIcon(icon2)
        self.btn_max.setIconSize(QtCore.QSize(36, 36))
        self.btn_max.setObjectName("btn_max")
        self.horizontalLayout_2.addWidget(self.btn_max)
        self.btn_normal = QtWidgets.QPushButton(self.frame_superior)
        self.btn_normal.setMinimumSize(QtCore.QSize(36, 36))
        self.btn_normal.setMaximumSize(QtCore.QSize(36, 36))
        self.btn_normal.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/chevrons-down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_normal.setIcon(icon3)
        self.btn_normal.setIconSize(QtCore.QSize(36, 36))
        self.btn_normal.setObjectName("btn_normal")
        self.horizontalLayout_2.addWidget(self.btn_normal)
        self.btn_cerrar = QtWidgets.QPushButton(self.frame_superior)
        self.btn_cerrar.setMinimumSize(QtCore.QSize(36, 36))
        self.btn_cerrar.setMaximumSize(QtCore.QSize(36, 36))
        self.btn_cerrar.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(230,0,0);\n"
"}")
        self.btn_cerrar.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cerrar.setIcon(icon4)
        self.btn_cerrar.setIconSize(QtCore.QSize(36, 36))
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.horizontalLayout_2.addWidget(self.btn_cerrar)
        self.verticalLayout.addWidget(self.frame_superior)
        self.frame_contenido = QtWidgets.QFrame(self.frame)
        self.frame_contenido.setStyleSheet("background-color: rgb(255,255,255);\n"
"border-radius: 10px;")
        self.frame_contenido.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_contenido.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_contenido.setObjectName("frame_contenido")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_contenido)
        self.horizontalLayout_3.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_menu = QtWidgets.QFrame(self.frame_contenido)
        self.frame_menu.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_menu.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_menu.setStyleSheet("QFrame{\n"
"background-color: rgb(230, 240, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(84,111,236);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"color:rgb(255, 255, 255);\n"
"font: 77 12pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(39,74,233);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 77 12pt \"Arial Black\";\n"
"border-top-right-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"color:rgb(84,111,236);\n"
"font: 77 12pt \"Arial Black\";\n"
"}\n"
"")
        self.frame_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu.setObjectName("frame_menu")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_menu)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_menu)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.comboBox_puerto = QtWidgets.QComboBox(self.frame_menu)
        self.comboBox_puerto.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox_puerto.setStyleSheet("QComboBox{\n"
"border:3px solid #111111;\n"
"border-radius: 5px;\n"
"min-width: 6em;\n"
"background-color: rgb(230, 240, 255);\n"
"font: 87 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"subcontrol-origin:padding;\n"
"subcontrol-position: top right;\n"
"width: 15px;\n"
"border-left-width: 3px;\n"
"border-left-color:#111111;\n"
"border-left-style:solid;\n"
"border-top-right-radius: 4px;\n"
"border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"background:#2c2c2c;\n"
"selection-background-color:#ff0037;\n"
"color:rgb(218,0,55);\n"
"}")
        self.comboBox_puerto.setObjectName("comboBox_puerto")
        self.horizontalLayout_4.addWidget(self.comboBox_puerto)
        self.btn_actualizar = QtWidgets.QPushButton(self.frame_menu)
        self.btn_actualizar.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_actualizar.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_actualizar.setStyleSheet("border-radius:18px;")
        self.btn_actualizar.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/rotate-cw (1).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_actualizar.setIcon(icon5)
        self.btn_actualizar.setIconSize(QtCore.QSize(25, 25))
        self.btn_actualizar.setObjectName("btn_actualizar")
        self.horizontalLayout_4.addWidget(self.btn_actualizar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 81, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_menu)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.comboBox_velocidad = QtWidgets.QComboBox(self.frame_menu)
        self.comboBox_velocidad.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox_velocidad.setMaximumSize(QtCore.QSize(220, 16777215))
        self.comboBox_velocidad.setStyleSheet("QComboBox{\n"
"border:3px solid #111111;\n"
"border-radius: 5px;\n"
"min-width: 6em;\n"
"background-color: rgb(230, 240, 255);\n"
"font: 87 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"subcontrol-origin:padding;\n"
"subcontrol-position: top right;\n"
"width: 15px;\n"
"border-left-width: 3px;\n"
"border-left-color:#111111;\n"
"border-left-style:solid;\n"
"border-top-right-radius: 4px;\n"
"border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"background:#2c2c2c;\n"
"selection-background-color:#ff0037;\n"
"color:rgb(218,0,55);\n"
"}")
        self.comboBox_velocidad.setObjectName("comboBox_velocidad")
        self.verticalLayout_2.addWidget(self.comboBox_velocidad)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 82, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem7 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_conectar = QtWidgets.QPushButton(self.frame_menu)
        self.btn_conectar.setMinimumSize(QtCore.QSize(190, 50))
        self.btn_conectar.setMaximumSize(QtCore.QSize(190, 50))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/log-in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_conectar.setIcon(icon6)
        self.btn_conectar.setIconSize(QtCore.QSize(30, 30))
        self.btn_conectar.setObjectName("btn_conectar")
        self.verticalLayout_4.addWidget(self.btn_conectar)
        self.btn_desconectar = QtWidgets.QPushButton(self.frame_menu)
        self.btn_desconectar.setMinimumSize(QtCore.QSize(190, 50))
        self.btn_desconectar.setMaximumSize(QtCore.QSize(190, 50))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_desconectar.setIcon(icon7)
        self.btn_desconectar.setIconSize(QtCore.QSize(30, 30))
        self.btn_desconectar.setObjectName("btn_desconectar")
        self.verticalLayout_4.addWidget(self.btn_desconectar)
        self.horizontalLayout_9.addLayout(self.verticalLayout_4)
        spacerItem8 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        spacerItem9 = QtWidgets.QSpacerItem(20, 81, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem10 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem10)
        self.label = QtWidgets.QLabel(self.frame_menu)
        self.label.setMinimumSize(QtCore.QSize(150, 150))
        self.label.setMaximumSize(QtCore.QSize(150, 150))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/escudo_negativo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label)
        spacerItem11 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem11)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_3.addWidget(self.frame_menu)
        self.frame_paginas = QtWidgets.QFrame(self.frame_contenido)
        self.frame_paginas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_paginas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_paginas.setObjectName("frame_paginas")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_paginas)
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 20)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem12 = QtWidgets.QSpacerItem(165, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem12)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_videocapture = QtWidgets.QLabel(self.frame_paginas)
        self.label_videocapture.setMinimumSize(QtCore.QSize(640, 480))
        self.label_videocapture.setMaximumSize(QtCore.QSize(640, 480))
        self.label_videocapture.setText("")
        self.label_videocapture.setPixmap(QtGui.QPixmap("icons/day-of-the-dead-skull-and-bones-flat-by-Vexels.png"))
        self.label_videocapture.setScaledContents(True)
        self.label_videocapture.setObjectName("label_videocapture")
        self.verticalLayout_6.addWidget(self.label_videocapture)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem13)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem14)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_iniciar = QtWidgets.QPushButton(self.frame_paginas)
        self.btn_iniciar.setMinimumSize(QtCore.QSize(180, 50))
        self.btn_iniciar.setMaximumSize(QtCore.QSize(180, 50))
        self.btn_iniciar.setStyleSheet("QPushButton{\n"
"background-color: rgb(84,111,236);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"color:rgb(255, 255, 255);\n"
"font: 77 12pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(39,74,233);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 77 12pt \"Arial Black\";\n"
"border-top-right-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"color:rgb(84,111,236);\n"
"font: 77 12pt \"Arial Black\";\n"
"}\n"
"")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/user-check.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_iniciar.setIcon(icon8)
        self.btn_iniciar.setIconSize(QtCore.QSize(30, 30))
        self.btn_iniciar.setObjectName("btn_iniciar")
        self.horizontalLayout_7.addWidget(self.btn_iniciar)
        self.btn_detener = QtWidgets.QPushButton(self.frame_paginas)
        self.btn_detener.setMinimumSize(QtCore.QSize(180, 50))
        self.btn_detener.setMaximumSize(QtCore.QSize(180, 50))
        self.btn_detener.setStyleSheet("QPushButton{\n"
"background-color: rgb(84,111,236);\n"
"border-top-right-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"border-top-left-radius:5px;\n"
"border-bottom-left-radius:5px;\n"
"color:rgb(255, 255, 255);\n"
"font: 77 12pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(39,74,233);\n"
"border-top-right-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 77 12pt \"Arial Black\";\n"
"border-top-left-radius:5px;\n"
"border-bottom-left-radius:5px;\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"color:rgb(84,111,236);\n"
"font: 77 12pt \"Arial Black\";\n"
"}\n"
"")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/user-x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_detener.setIcon(icon9)
        self.btn_detener.setIconSize(QtCore.QSize(30, 30))
        self.btn_detener.setObjectName("btn_detener")
        self.horizontalLayout_7.addWidget(self.btn_detener)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem15)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_11.addLayout(self.verticalLayout_6)
        spacerItem16 = QtWidgets.QSpacerItem(165, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem16)
        self.horizontalLayout_3.addWidget(self.frame_paginas)
        self.verticalLayout.addWidget(self.frame_contenido)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Puerto Serial"))
        self.label_4.setText(_translate("MainWindow", "Velocidad"))
        self.btn_conectar.setText(_translate("MainWindow", " Conectar"))
        self.btn_desconectar.setText(_translate("MainWindow", "Desconectar"))
        self.btn_iniciar.setText(_translate("MainWindow", "  Iniciar"))
        self.btn_detener.setText(_translate("MainWindow", "  Detener"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
