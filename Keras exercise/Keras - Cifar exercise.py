from keras.datasets import cifar10
from keras.utils import np_utils
from keras.models import Sequential
from keras import layers
import random
import numpy as np
import cv2

label_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Wczytywanie danych
num_pixels = x_train[1] * x_train[2] * x_train[3]

# spłaszczenie danych z 3d (32x32x3) do 1d

x_train = x_train.reshape((50000,32,32,3))
x_train = x_train.astype('float32') / 255
x_test = x_test.reshape((10000,32,32,3))
x_test = x_test.astype('float32') / 255

# Tworzenie listy klas
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

# Tworzenie modelu sieci
model = Sequential()

model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
# model.add(layers.Conv2D(32, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# model.add(layers.Flatten())

model.add(layers.Dense(10, activation='softmax'))


# Kompilacja modelu
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Uczenie modelu danymi
# epoch - liczba iteracji
# batch_size - liczba elemenów z danych treningowych branych podczas pojedyńczego przejścia funkcji uczącej
history = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=50, batch_size=500, verbose=1)

# Testowanie modelu
scores = model.evaluate(x_test, y_test, verbose=0)
print("Baseline Error: %.2f%%" % (100-scores[1]*100))

model.summary()


random_number = random.randint(0, 50000)

result = model.predict(x_train[random_number].reshape(1, 32, 32, 3), batch_size=1)
predicted_class = np.where(result[0] == result[0].max())
print(label_names[predicted_class[0][0]])

cv2.imshow('Check if the function works!!', x_train[random_number])
cv2.waitKey(0)





