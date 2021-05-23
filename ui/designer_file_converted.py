# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaceGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ventana(object):
    def setupUi(self, ventana):
        ventana.setObjectName("ventana")
        ventana.resize(853, 549)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icono/img/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ventana.setWindowIcon(icon)
        ventana.setWindowOpacity(1.0)
        self.graficoDeBarras = QtWidgets.QPushButton(ventana)
        self.graficoDeBarras.setGeometry(QtCore.QRect(680, 90, 161, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.graficoDeBarras.setFont(font)
        self.graficoDeBarras.setObjectName("graficoDeBarras")
        self.graficoDeDispercion = QtWidgets.QPushButton(ventana)
        self.graficoDeDispercion.setGeometry(QtCore.QRect(680, 120, 161, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.graficoDeDispercion.setFont(font)
        self.graficoDeDispercion.setObjectName("graficoDeDispercion")
        self.cargarMapa = QtWidgets.QPushButton(ventana)
        self.cargarMapa.setGeometry(QtCore.QRect(710, 300, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cargarMapa.setFont(font)
        self.cargarMapa.setStyleSheet("background-color: rgb(60, 63, 65);\n"
"color: rgb(255, 255, 255);")
        self.cargarMapa.setObjectName("cargarMapa")
        self.title = QtWidgets.QLabel(ventana)
        self.title.setGeometry(QtCore.QRect(230, 10, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.labelUrbano = QtWidgets.QLabel(ventana)
        self.labelUrbano.setGeometry(QtCore.QRect(16, 62, 641, 451))
        self.labelUrbano.setStyleSheet("border-image: url(:/imagen/img/b5.tif);")
        self.labelUrbano.setText("")
        self.labelUrbano.setTextFormat(QtCore.Qt.AutoText)
        self.labelUrbano.setObjectName("labelUrbano")
        self.labelRural = QtWidgets.QLabel(ventana)
        self.labelRural.setGeometry(QtCore.QRect(16, 62, 641, 451))
        self.labelRural.setStyleSheet("border-image: url(:/imagen/img/b4.tif);")
        self.labelRural.setText("")
        self.labelRural.setObjectName("labelRural")
        self.labelBarras = QtWidgets.QLabel(ventana)
        self.labelBarras.setGeometry(QtCore.QRect(16, 62, 641, 451))
        self.labelBarras.setStyleSheet("border-image: url(:/graficoBarras/img/graficoBarras.png);")
        self.labelBarras.setText("")
        self.labelBarras.setObjectName("labelBarras")
        self.confirmacionUNO = QtWidgets.QLabel(ventana)
        self.confirmacionUNO.setGeometry(QtCore.QRect(680, 350, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.confirmacionUNO.setFont(font)
        self.confirmacionUNO.setAcceptDrops(False)
        self.confirmacionUNO.setStyleSheet("color: rgb(255, 255, 255);")
        self.confirmacionUNO.setObjectName("confirmacionUNO")
        self.confirmacionDOS = QtWidgets.QLabel(ventana)
        self.confirmacionDOS.setGeometry(QtCore.QRect(680, 410, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.confirmacionDOS.setFont(font)
        self.confirmacionDOS.setAcceptDrops(False)
        self.confirmacionDOS.setStyleSheet("color: rgb(255, 255, 255);")
        self.confirmacionDOS.setObjectName("confirmacionDOS")

        self.retranslateUi(ventana)
        QtCore.QMetaObject.connectSlotsByName(ventana)

    def retranslateUi(self, ventana):
        _translate = QtCore.QCoreApplication.translate
        ventana.setWindowTitle(_translate("ventana", "Clasificación del suelo Mónaco"))
        self.graficoDeBarras.setText(_translate("ventana", "Grafico de Barras"))
        self.graficoDeDispercion.setText(_translate("ventana", "Grafico de Dispersión"))
        self.cargarMapa.setText(_translate("ventana", "Cargar bandas"))
        self.title.setText(_translate("ventana", "Análisis Mónaco"))
        self.confirmacionUNO.setText(_translate("ventana", "El archivo se cargó\n"
"correctamente"))
        self.confirmacionDOS.setText(_translate("ventana", "Por favor seleccione\n"
"la otra banda"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = QtWidgets.QDialog()
    ui = Ui_ventana()
    ui.setupUi(ventana)
    ventana.show()
    sys.exit(app.exec_())

