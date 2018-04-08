# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 20:32:35 2018

@author: diane
"""

import keras
#from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.optimizers import adam, sgd
import tron_helper
import numpy as np
from sklearn.model_selection import train_test_split
from numpy.random import seed
from tensorflow import set_random_seed

batch_size = 128
num_classes = 2
epochs = 5
#set keras' random seed for reproducibility
seed(3)
#set tensorflow's random seed for reproducibility
set_random_seed(3)

print("epochs: ", epochs)
x_train = []
x_test = []
y_train = []
y_test = []
#the data shuffled and split between train and test sets
(x_train, y_train) = tron_helper.format_input_data('training_data.dat')
x_train, x_test = train_test_split(x_train, train_size=0.8, test_size = 0.2)
y_train, y_test = train_test_split(y_train, train_size=0.8, test_size = 0.2)
print(x_train[0])
print(y_train[0])
#right now using same data set for training and testing
#(x_test, y_test) = tron_helper.format_input_data('training_data.dat')
#print('\n')
print(x_test[0])
print(y_test[0])
#format as numpy arrays
x_train = np.array(x_train, dtype=np.float32)
y_train = np.array(y_train, dtype=np.float32)
x_test = np.array(x_test, dtype=np.float32)
y_test = np.array(y_test, dtype=np.float32)
#x_train = x_train.astype('float32')
#x_test = x_test.astype('float32')

print(x_train.shape[0], 'total samples')
#print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
#y_train = keras.utils.to_categorical(y_train, num_classes)
#y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()
#model.add(Dense(512, activation='relu', input_shape=(784,)))
#diane - this will be 400 when board is 20 x 20
model.add(Dense(100, activation='relu', input_shape=(100,)))
#model.add(Dropout(0.2))
model.add(Dense(50, activation='relu'))
model.add(Dense(4, activation='relu'))
#model.add(Dropout(0.2))
#

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=0,
                    validation_data=(x_test, y_test))

score = model.evaluate(x_test, y_test, verbose=0)
#score = model.evaluate(verbose=0, steps = 3)
model.save_weights('tron_wts.h5')
print('Test loss:', score[0])
print('Test accuracy:', score[1])