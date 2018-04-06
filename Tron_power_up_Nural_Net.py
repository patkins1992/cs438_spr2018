"""
Created on Thu Jan 18 14:59:05 2018
@author: Justin Deterding
"""

from Tron import Grid 
from Tron import Player
from Justins_player import Open_Dist_Player
from matplotlib import pyplot as plt
from sklearn.neural_network import MLPClassifier
import numpy as np

def plot_grid(fig):
    plt.draw()
    plt.pause(.01)
    fig.canvas.draw_idle()  
    fig.canvas.flush_events()
    

grid_size=10    #Create a grid of size grid_size

clf = MLPClassifier(solver='lbfgs',
          hidden_layer_sizes=(15,), random_state=1)


n=0
while n < 1100:#number of rounds
    print("Number of Traing example: "+str(n))
    if n> 1000:
        input("n > 1000 reached. Press Enter to continue...")
        
    board_states=[]     #List to keep track of board states per round
    player_decisions=[] #List to keep track of player desisions per round
    #Initilize the list of players to play on the grid
    list_of_player=[Open_Dist_Player('r'),
                    Open_Dist_Player('b')]
    #Create new grid
    the_grid = Grid(list_of_player,grid_size=grid_size)
    #prep the the figure to plot the game
    fig = the_grid.display_the_grid()
    plt.ion()
    the_grid.display_the_grid(fig=fig)
    plot_grid(fig)
    while the_grid.active_players.__len__() > 1:#Loop untill no players remain
        the_grid.display_the_grid(fig=fig)
        plot_grid(fig)
  
        if n > 0:
            print("P:[[L,R,U,D]]")
        
        x=[]
        for player in the_grid.active_players:
            g=the_grid.get_grid(player.node)
            x.append(g)
            if n > 0:
                print(player.color, end=": ")
                print(clf.predict_proba([g]))
        board_states.append(x)
        moves = the_grid.move_players()
        player_decisions.append(moves)
        fig.show()           
    #draw the last moves
    the_grid.display_the_grid(fig=fig)
    plot_grid(fig)
    #print the winner
    if the_grid.active_players.__len__() == 0:
        print("Sorry folks, looks like theres not a winner today.")
    else:
        print("The Winner is " +the_grid.active_players[0].color+" !")
        X=[];   y=[];  i=1
        if the_grid.active_players[0].color == 'r':
            i=0  
        for state in board_states:
                X.append(state[i])
        for decision in player_decisions:
            y.append(decision[i])
        n+=X.__len__()
        clf.fit(X, y)
    plt.close(fig)

plt.ioff()


