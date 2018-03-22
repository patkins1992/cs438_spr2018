"""
Created on Thu Jan 18 14:59:05 2018
@author: Justin Deterding
"""

from Tron import Grid 
from Tron import Player
from Justins_player import Open_Dist_Player
from matplotlib import pyplot as plt


#Create a grid of size grid_size
grid_size=10
#Initilize the list of players to play on the grid
list_of_player=[Open_Dist_Player('r'),Open_Dist_Player('b'),Open_Dist_Player('g'),Player('c'),
                Player('m'),Player('y')]
               
#Create grid
the_grid = Grid(list_of_player,grid_size=grid_size)

#prep the the figure to plot the game
fig = the_grid.display_the_grid()
plt.ion()
the_grid.display_the_grid(fig=fig)
plt.draw()
plt.pause(.01)
fig.canvas.draw_idle()  
fig.canvas.flush_events()
#Loop untill no players remain
while the_grid.active_players.__len__() > 1:
    the_grid.display_the_grid(fig=fig)
    plt.draw()
    plt.pause(.01)
    fig.canvas.draw_idle()  
    fig.canvas.flush_events()
#   Print What the players see move by move    
#    print("----------------------------------")
#    for player in the_grid.active_players:
#        print("Player: "+player.color, end=" : ")
#        for item in player.look_sense():
#            print(item, end=" :")
#        print()
    the_grid.move_players()
   
#draw the last moves
the_grid.display_the_grid(fig=fig)
plt.draw()
plt.pause(.01)
fig.canvas.draw_idle()
fig.canvas.flush_events()
plt.ioff()

#print the winner
if the_grid.active_players.__len__() == 0:
    print("Sorry folks, looks like theres not a winner today.")
else:
    print("The Winner is " +the_grid.active_players[0].color+" !")