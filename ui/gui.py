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

        self.filtroRural = QtWidgets.QPushButton(ventana)
        self.filtroRural.setGeometry(QtCore.QRect(680, 120, 161, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filtroRural.setFont(font)
        self.filtroRural.setStyleSheet("color: rgb(230, 230, 230);")
        self.filtroRural.setObjectName("filtroRural")

        self.filtroUrbano = QtWidgets.QPushButton(ventana)
        self.filtroUrbano.setGeometry(QtCore.QRect(680, 90, 161, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filtroUrbano.setFont(font)
        self.filtroUrbano.setStyleSheet("color: rgb(230, 230, 230);")
        self.filtroUrbano.setObjectName("filtroUrbano")

        self.graficoDeBarras = QtWidgets.QPushButton(ventana)
        self.graficoDeBarras.setGeometry(QtCore.QRect(680, 150, 161, 23))
        self.graficoDeBarras.clicked.connect(self.showBarras)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.graficoDeBarras.setFont(font)
        self.graficoDeBarras.setStyleSheet("color: rgb(230, 230, 230);")
        self.graficoDeBarras.setObjectName("graficoDeBarras")

        self.graficoDeDispercion = QtWidgets.QPushButton(ventana)
        self.graficoDeDispercion.setGeometry(QtCore.QRect(680, 180, 161, 23))
        self.graficoDeDispercion.clicked.connect(self.showDispercion)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.graficoDeDispercion.setFont(font)
        self.graficoDeDispercion.setStyleSheet("color: rgb(230, 230, 230);")
        self.graficoDeDispercion.setObjectName("graficoDeDispercion")

        self.cargarMapa = QtWidgets.QPushButton(ventana)
        self.cargarMapa.clicked.connect(self.Cargar)
        # self.cargarMapa.clicked.connect(self.loadTif)
        self.cargarMapa.setGeometry(QtCore.QRect(710, 310, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cargarMapa.setFont(font)
        self.cargarMapa.setStyleSheet("color: rgb(230, 230, 230);")
        self.cargarMapa.setText("Cargar banda")
        self.cargarMapa.setObjectName("cargarMapa")

        self.graficoDeConfucion = QtWidgets.QPushButton(ventana)
        self.graficoDeConfucion.setGeometry(QtCore.QRect(680, 210, 161, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.graficoDeConfucion.setFont(font)
        self.graficoDeConfucion.setStyleSheet("color: rgb(230, 230, 230);")
        self.graficoDeConfucion.setObjectName("graficoDeConfucion")

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
        self.filtroRural.setText(_translate("ventana", "Filtro Rural"))
        self.filtroUrbano.setText(_translate("ventana", "Filtro Urbano"))
        self.graficoDeBarras.setText(_translate("ventana", "Grafico de Barras"))
        self.graficoDeDispercion.setText(_translate("ventana", "Grafico de Dispersión"))
        self.cargarMapa.setText(_translate("ventana", "Cargar Mapa"))
        self.graficoDeConfucion.setText(_translate("ventana", "Grafico de Confución"))
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

        '''
        if nombreImagen:
            # Verificar que QLabel tiene imagen
            labelConImagen = ""
            if self.labelMapa.pixmap():
                labelConImagen = self.labelImagen

            imagen = QImage(nombreImagen)
            if imagen.isNull():
                if labelConImagen:
                    self.Eliminar()

                QMessageBox.information(self, "Visor de imágenes",
                                        "No se puede cargar %s." % nombreImagen)
                return

            # Obtener ruta de la carpeta que contiene la imagen seleccionada
            self.carpetaActual = QDir(QFileInfo(nombreImagen).absoluteDir().path())

            # Obtener la ruta y el nombre de las imagenes que se encuentren en la carpeta de
            # la imagen seleccionada
            imagenes = self.carpetaActual.entryInfoList(["*.tif"],
                                                        QDir.Files, QDir.Name)
            self.imagenesCarpeta = [imagen.absoluteFilePath() for imagen in imagenes]

            self.posicion = self.imagenesCarpeta.index(nombreImagen)
            self.estadoAnterior = True if self.posicion == 0 else False
            self.estadoSiguiente = True if self.posicion == len(self.imagenesCarpeta) - 1 else False

            # Nombre y extensión de la imagen
            nombre = QFileInfo(nombreImagen).fileName()

            if labelConImagen:
                posicionInternaX = -650
                labelMostrarImagen = self.labelImagen if self.labelImagenUno.pixmap() else self.labelImagenUno
                self.Limpiar(labelConImagen, labelMostrarImagen, imagen, nombre, posicionInternaX)
            else:
                self.Mostrar(self.labelMapa, imagen, nombre)
        '''

# ====================== CLASE visorImagenes =======================

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
