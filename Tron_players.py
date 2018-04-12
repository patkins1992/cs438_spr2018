# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:26:03 2018

@author: Justin Deterding
"""
from Tron import Player
import tron_helper
import keras.models
import numpy as np

model = keras.models.load_model('tron_wts.h5')

class Open_Dist_Player(Player):
    def move(self):
        look = self.look_sense()
        max_open_dist=-1
        for direction in look:
            if(max_open_dist<direction[1]):
                max_open_dist = direction[1]
                move_direction= direction[0]
        return self.directional_move(move_direction)

class NN_Player(Player):
    def move(self):
        #get the board state
        n=self.node
        board_state = self.grid.get_grid(n, value=(1, 0.5, 0))
        #format the board state so the neural net can use it to predict the best move
        board_state = [board_state] #neural net needs list containing list that contains board state
        board_state = np.array(board_state)
        #ask the neural net to predict the move based on the board state
        move_direction = model.predict(board_state)
        #print(move_direction)
        #interpret the prediction
        #the result is a set of 4 floats, [left right up down]
        max_prob = move_direction.argmax()
        if max_prob == 0:
            interpreted_move_direction = 'left'
        elif max_prob == 1:
            interpreted_move_direction = 'right'
        elif max_prob == 2:
            interpreted_move_direction = 'up'
        elif max_prob == 3:
            interpreted_move_direction = 'down'
        #print(interpreted_move_direction)
        return self.directional_move(interpreted_move_direction)