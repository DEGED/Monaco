# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaceGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import numpy
from numpy import array
from PyQt5 import QtCore
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import (Qt, QDir, QFileInfo)
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (QMainWindow, QMessageBox,
                             QLabel, QFileDialog)

class Ui_ventana(QMainWindow):
    a = array([])

    def setupUi(self, ventana):
        ventana.setObjectName("ventana")
        ventana.resize(853, 549)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/icon.ico"))
        ventana.setWindowIcon(icon)
        ventana.setWindowOpacity(1.0)
        ventana.setStyleSheet("background-color: rgb(43, 43, 43);")

        self.graficoDeBarras = QtWidgets.QPushButton(ventana)
        self.graficoDeBarras.setGeometry(QtCore.QRect(680, 90, 161, 25))
        self.graficoDeBarras.clicked.connect(self.showBarras)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.graficoDeBarras.setFont(font)
        self.graficoDeBarras.setStyleSheet("background-color: rgb(60, 63, 65);\n""color: rgb(230, 230, 230);")
        self.graficoDeBarras.setObjectName("graficoDeBarras")

        self.graficoDeDispercion = QtWidgets.QPushButton(ventana)
        self.graficoDeDispercion.setGeometry(QtCore.QRect(680, 120, 161, 25))
        self.graficoDeDispercion.clicked.connect(self.showDispercion)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.graficoDeDispercion.setFont(font)
        self.graficoDeDispercion.setStyleSheet("background-color: rgb(60, 63, 65);\n""color: rgb(230, 230, 230);")
        self.graficoDeDispercion.setObjectName("graficoDeDispercion")

        self.cargarMapa = QtWidgets.QPushButton(ventana)
        self.cargarMapa.clicked.connect(self.Cargar)
        # self.cargarMapa.clicked.connect(self.loadTif)
        self.cargarMapa.setGeometry(QtCore.QRect(710, 300, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cargarMapa.setFont(font)
        self.cargarMapa.setStyleSheet("background-color: rgb(60, 63, 65);\n""color: rgb(255, 255, 255);")
        self.cargarMapa.setText("Cargar banda")
        self.cargarMapa.setObjectName("cargarMapa")

        self.title = QtWidgets.QLabel(ventana)
        self.title.setGeometry(QtCore.QRect(230, 10, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(230, 230, 230);")
        self.title.setObjectName("title")

        self.labelUrbano = QtWidgets.QLabel(ventana)
        self.labelUrbano.setGeometry(QtCore.QRect(16, 62, 641, 451))
        # self.labelUrbano.setStyleSheet("border-image: url(:/imagen/img/b5.tif);")
        self.labelUrbano.setText("")
        self.labelUrbano.setTextFormat(QtCore.Qt.AutoText)
        self.labelUrbano.setObjectName("labelUrbano")
        self.labelRural = QtWidgets.QLabel(ventana)
        self.labelRural.setGeometry(QtCore.QRect(16, 62, 641, 451))
        # self.labelRural.setStyleSheet("border-image: url(:/imagen/img/b4.tif);")
        self.labelRural.setText("")
        self.labelRural.setObjectName("labelRural")

        self.labelMapa = QtWidgets.QLabel(ventana)
        self.labelMapa.setGeometry(QtCore.QRect(16, 62, 641, 451))
        self.labelMapa.setText("")
        self.labelMapa.setObjectName("labelMapa")

        self.diagramBarras = QtWidgets.QLabel(ventana)
        self.diagramBarras.setGeometry(QtCore.QRect(16, 62, 641, 451))
        self.diagramBarras.setText("")
        self.diagramBarras.setObjectName("diagram")

        self.diagramDispercion = QtWidgets.QLabel(ventana)
        self.diagramDispercion.setGeometry(QtCore.QRect(16, 62, 641, 451))
        self.diagramDispercion.setText("")
        self.diagramDispercion.setObjectName("diagram")

        self.retranslateUi(ventana)
        QtCore.QMetaObject.connectSlotsByName(ventana)

    def showDispercion(self):
        self.diagramDispercion.setVisible(True)
        self.diagramBarras.setVisible(False)
        self.diagramDispercion.setStyleSheet("border-image: url(img/graficoDispercion.png);")

    def showBarras(self):
        self.diagramBarras.setVisible(True)
        self.diagramDispercion.setVisible(False)
        self.diagramBarras.setStyleSheet("border-image: url(img/graficoBarras.jpg);")

    def retranslateUi(self, ventana):
        _translate = QtCore.QCoreApplication.translate
        ventana.setWindowTitle(_translate("ventana", "Clasificación del suelo Mónaco"))
        self.graficoDeBarras.setText(_translate("ventana", "Grafico de Barras"))
        self.graficoDeDispercion.setText(_translate("ventana", "Grafico de Dispersión"))
        self.title.setText(_translate("ventana", "Análisis Mónaco"))

    def Mostrar(self, label, imagen, nombre, posicionX=650):
        imagen = QPixmap.fromImage(imagen)

        # Escalar imagen a 640x480 si el ancho es mayor a 640 o el alto mayor a 480
        if imagen.width() > 640 or imagen.height() > 480:
            imagen = imagen.scaled(640, 480, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Mostrar imagen
        label.setPixmap(imagen)

    def Cargar(self):
        nombreImagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen",
                                                      QDir.currentPath(),
                                                      "Archivos de imagen (*.tif)")

        self.a = numpy.append(self.a, nombreImagen)

        if len(self.a) >= 2:
            self.cargarMapa.setDisabled(True)



class visorImagenes(QMainWindow):
    def __init__(self, parent=None):
        super(visorImagenes, self).__init__(parent)

        self.setWindowTitle("CargarImagen")
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(682, 573)
        self.initUI()

    def initUI(self):
        widget = Ui_ventana(self)
        self.setCentralWidget(widget)
        labelVersion = QLabel(self)
        labelVersion.setText(" Vima versión beta: 1.0  ")
        self.statusBar = self.statusBar()
        self.statusBar.addPermanentWidget(labelVersion, 0)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ventana = QtWidgets.QDialog()
    ui = Ui_ventana()
    ui.setupUi(ventana)
    ventana.show()
    sys.exit(app.exec_())
