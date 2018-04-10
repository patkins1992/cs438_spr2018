# https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
# Create your first MLP in Keras
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
from tron_helper import format_input_data
# fix random seed for reproducibility
np.random.seed(7)
# load pima indians dataset
dataset = format_input_data("test.txt")
# split into input (X) and output (Y) variables
X = np.array(dataset[0])
Y = np.array(dataset[1])
# create model
model = Sequential()
model.add(Dense(12, input_dim=4, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(4, activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, epochs=150, batch_size=10)
# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))