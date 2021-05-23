import numpy as np
from PIL import Image
import pandas as pd
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
    print("prediciendo")
    model = joblib.load('monacoEntrenado.joblib')
    print("modelo cargado")
    data = cargar2(pathbanda4, pathbanda5)
    print("vojabes")
    print(data)

    predictions = model.predict(data)

    return predictions

def listar(matrix):
    resultado = []
    for lista in matrix:
        for object in lista:
            resultado.append(object)


    return resultado


