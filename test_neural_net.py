# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 20:32:35 2018

@author: diane
"""

import keras
#from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import adam, SGD, adadelta
from keras import initializers
import tron_helper
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import linear_model
from numpy.random import seed
from tensorflow import set_random_seed
import matplotlib.pyplot as plt

batch_size = 128
#num_classes = 4
epochs = 120
#set keras' random seed for reproducibility
seed(3)
#set tensorflow's random seed for reproducibility
set_random_seed(3)

#print("epochs: ", epochs)
#get the input (x_train), and the training output (y_train)
(x_train, y_train) = tron_helper.format_input_data('test_1.txt')
print(x_train.shape[0], 'total samples')

model = Sequential()
#model.add(Dense(512, activation='relu', input_shape=(784,)))
#diane - this will be 400 when board is 20 x 20
model.add(Dense(300, activation='relu', input_shape=(100,)))
#model.add(Dropout(0.2))
model.add(Dense(120, activation='relu'))
model.add(Dense(4, activation='sigmoid'))
#model.add(Dropout(0.2))

model.summary()

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1)

model.save_weights('tron_wts.h5')