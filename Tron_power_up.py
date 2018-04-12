"""
Created on Thu Jan 18 14:59:05 2018
@author: Justin Deterding
"""

from Tron import Grid 
from Tron_players import Open_Dist_Player, NN_Player
from matplotlib import pyplot as plt


#Create a grid of size grid_size
grid_size=10
#Initilize the list of players to play on the grid
list_of_player=[Open_Dist_Player('r'),NN_Player('b')]#,Open_Dist_Player('g'),Player('c'),
               # Player('m'),Player('y')]
               
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
    fig.show()
    if the_grid.active_players.__len__()>0:
        n=the_grid.active_players[0].node
        grid_pic=the_grid.get_grid(n)
        print('----------------------------')
        for row in  grid_pic:
            print(row)
   
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