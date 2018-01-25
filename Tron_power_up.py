# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:59:05 2018

@author: Justin Deterding
"""

from Tron import Grid 
from Tron import Player
from My_player import My_Player
#import numpy as np
from matplotlib import pyplot as plt
#rom matplotlib import animation

grid_size=1000

fig = plt.figure()
ax =plt.axes(xlim=(-1,grid_size+1),ylim=(-1,grid_size+1))

# Generate a Grid
list_of_player=[Player(),Player(),My_Player()]

list_of_player[0].color='r'
list_of_player[1].color='b'
list_of_player[2].color='g'

the_grid = Grid(list_of_player,grid_size=grid_size)
while the_grid.active_players.__len__() > 1:
    the_grid.move_players()

   
ax.plot(the_grid.players_path[0][1],the_grid.players_path[0][2],the_grid.players_path[0][0].color)
ax.plot(the_grid.players_path[1][1],the_grid.players_path[1][2],the_grid.players_path[1][0].color)
ax.plot(the_grid.players_path[2][1],the_grid.players_path[2][2],the_grid.players_path[2][0].color)

for player in the_grid.active_players:
    print("The Winner is " +player.color+" !")