
# Implementacja obsługi ładowania i predykcji modelu

import os
import keras.models
import cv2
import numpy as np

from PyQt5.QtGui import QImage, QPainter, QPen, QBrush, QPixmap

def qimage_to_array(image):
    """
    Funkcja konwertująca obiekt QImage do numpy array
    """
    image = image.convertToFormat(QImage.Format_Grayscale8)
    ptr = image.bits()
    ptr.setsize(image.byteCount())
    numpy_array = np.array(ptr).reshape(image.height(), image.width(), 1)

    # wykorzystanie bibloteki OpenCV do wyświetlenia obrazu po konwersji
    # cv2.imshow('Check if the function works!', numpy_array)
    return numpy_array
    



def predict(image, model):
    """
    Funkcja wykorzystująca załadowany model sieci neuronowej do predykcji znaku na obrazie 

    Należy dodać w niej odpowiedni kod do obsługi załadowanego modelu
    """
    numpy_array = qimage_to_array(image)

    # wykorzystanie bibloteki OpenCV do zmiany wielkości obrazu do wielkości obrazów używanych w zbiorze MNIST
    numpy_array = cv2.resize(numpy_array, (28,28))

    # wykorzystanie bibloteki OpenCV do wyświetlenia obrazu po konwersji
    # cv2.imshow('Check if the function works!!', numpy_array)

    result = model.predict(numpy_array.reshape(1,28,28,1), batch_size=1)
    print(result)

    predicted_number = np.where(result[0] == result[0].max())
    print(predicted_number)

    return predicted_number[0][0]


def get_model():
    """
    Funkcja wczytująca nauczony model sieci neuronowej

    Należy dodać w niej odpowiedni kod do wczytywania na modelu oraz wag
    """
    model = keras.models.load_model('keras_model')
    model.load_weights('keras_weights')

    return model