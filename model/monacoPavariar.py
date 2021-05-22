import numpy as np
from PIL import Image
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import joblib

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

    return predictions

def listar(matrix):
    resultado = []
    for lista in matrix:
        for object in lista:
            resultado.append(object)


    return resultado


vojabes = predecir( r'C:\Users\prestamo\PycharmProjects\Monaco\Monaco\img\b4.tif', r'C:\Users\prestamo\PycharmProjects\Monaco\Monaco\img\b4.tif')
print(vojabes)