from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import cv2
import joblib
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import rasterio

def mapa(band4Path):
    print("1")
    band4 = rasterio.open(band4Path)
    print("2")
   # band4Copy = band4
   # band4Copy = np.array(band4Copy.getdata()).reshape(band4Copy.size[1], band4Copy[0], 3)
    band4.dtypes
    print("3")
    band4.transform
    band4.crs
    plt.imshow(band4)

    plt.savefig(r'..\ui\img\mapa.png', dpi=None, facecolor='w',
                edgecolor='w',
                orientation='portrait', format=None,
                transparent=False, bbox_inches=None, pad_inches=0.1)
    print("4")
    image = cv2.imread(r'..\ui\img\mapa.png')
    original = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([22, 93, 0], dtype="uint8")
    upper = np.array([45, 255, 255], dtype="uint8")
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)
    plt.subplot(1, 2, 1)
    plt.imshow(mask, cmap="gray")
    plt.subplot(1, 2, 2)
    plt.imshow(output)


def cargar2(band4Path, band5Path):
    # Open the image
    band4 = Image.open(band4Path)
    band5 = Image.open(band5Path)

    try:
        red = np.asarray(band4, dtype='float64')
        nir = np.asarray(band5, dtype='float64')
        red = listar(red)
        nir = listar(nir)

    except SystemError:
        red = np.asarray(band4.getdata(), dtype='float64')
        nir = np.asarray(band5.getdata(), dtype='float64')

    data = {'red': red,'nir': nir}
    df = pd.DataFrame(data, columns = ['red', 'nir'])

    return df

def predecir(pathbanda4, pathbanda5, model):
    data = cargar2(pathbanda4, pathbanda5)
    predictions = model.predict(data)
    print(predictions)

    grafica(predictions)
    data['ndvi'] = predictions
    dispersion(data)
    print("0")
    #mapa(pathbanda4)
    return predictions

def listar(matrix):
    resultado = []
    for lista in matrix:
        for object in lista:
            resultado.append(object)


    return resultado

def grafica(df):

    urbano = [82068]
    noUrbano = [301155]

    numero_de_grupos = len(urbano)
    indice_barras = np.arange(numero_de_grupos)
    ancho_barras = 0.35

    plt.bar(indice_barras, urbano, width=ancho_barras, label='Urbano')
    plt.bar(indice_barras + ancho_barras, noUrbano, width=ancho_barras, label='No urbano')
    plt.legend(loc='best')
    ## Se colocan los indicadores en el eje x
    # plt.xticks(indice_barras + ancho_barras, ('Urbano','No urbano'))

    plt.ylabel('Cantidad')
    plt.xlabel('Clasificacion')
    plt.title('Clasificacion de suelo urbano vs no urbano')

    #plt.show()
    plt.savefig(r'..\ui\img\graficoBarras.jpg', dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1)



def dispersion(df):

    fig = plt.figure(figsize=(15, 9))
    ax = plt.axes()
    # We create the axes of the graph
    x = df['red'].values
    y = df['nir'].values
    z = df['ndvi'].values

    plt.plot(x, '.', color='red', label='red')
    plt.plot(y, '.', color='blue', label='nir')
    plt.plot(z, '.', color='green', label='ndvi')

    plt.title('Grafico dispersion dataset')
    plt.legend(loc='best')
    plt.savefig(r'..\ui\img\graficoDispercion.png', dpi=None, facecolor='w',
                edgecolor='w',
                orientation='portrait', format=None,
                transparent=False, bbox_inches=None, pad_inches=0.1)




