from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import joblib
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox


def cargar2(band4Path, band5Path):
    # Open the image
    band4 = Image.open(band4Path)
    band5 = Image.open(band5Path)
    print(band4)
    print(band5)
    #red = band4.read(1).astype('float64')
    #nir = band5.read(1).astype('float64')

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

def predecir(pathbanda4, pathbanda5):


    model = joblib.load('monacoEntrenado.joblib')

    data = cargar2(pathbanda4, pathbanda5)

    print(data)

    predictions = model.predict(data)

    grafica(predictions)
    data['ndvi'] = predictions
    dispersion(data)
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
    plt.savefig(r'C:\Users\prestamo\PycharmProjects\Monaco\ui\img\barras.png', dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)



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

    #plt.show()

    plt.savefig(r'C:\Users\prestamo\PycharmProjects\Monaco\ui\img\dispersion.png', dpi=None, facecolor='w',
                edgecolor='w',
                orientation='portrait', papertype=None, format=None,
                transparent=False, bbox_inches=None, pad_inches=0.1,
                frameon=None, metadata=None)



vojabes = predecir( r'C:\Users\prestamo\PycharmProjects\Monaco\ui\img\b4.tif', r'C:\Users\prestamo\PycharmProjects\Monaco\ui\img\b4.tif')
print(vojabes)