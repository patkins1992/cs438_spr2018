# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 20:32:35 2018

@author: diane
"""
import tron_helper
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import adam
from keras import initializers
from numpy.random import seed
from tensorflow import set_random_seed

batch_size = 128
#num_classes = 4
epochs = 30
#set keras' random seed for reproducibility
seed(3)
#set tensorflow's random seed for reproducibility
set_random_seed(3)

#print("epochs: ", epochs)
#get the input (x_train), and the training output (y_train)
(x_train, y_train) = tron_helper.format_input_data('board_state_input.txt')
print(x_train.shape[0], 'total samples')
model = Sequential()
#model.add(Dense(300, activation='relu', input_shape=(100,)))
model.add(Dense(40, activation='relu', input_shape=(4,)))
model.add(Dense(10, activation='relu'))
#model.add(Dense(40, activation='relu'))
model.add(Dense(4, activation='sigmoid'))
model.summary()

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['categorical_accuracy'])

history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1)

model.save('board_state_model.h5')