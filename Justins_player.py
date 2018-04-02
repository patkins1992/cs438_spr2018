# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:26:03 2018

@author: Justin Deterding
"""
from Tron import Player

class Open_Dist_Player(Player):
    def move(self):
        look = self.look_sense()
        max_open_dist=-1
        for direction in look:
            if(max_open_dist<direction[1]):
                max_open_dist = direction[1]
                move_direction= direction[0]       
        self.directional_move(move_direction)
        return
        

        
        