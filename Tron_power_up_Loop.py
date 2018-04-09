"""
Created on Thu Jan 18 14:59:05 2018
@author: Justin Deterding
"""
#--------------Imports--------------------------------------------------------
from Tron import Grid 
from Tron_players import Open_Dist_Player
from matplotlib import pyplot as plt
from tron_helper import append_data
#--------------Functions------------------------------------------------------
def plot_grid(fig):
    plt.draw()
    plt.pause(.01)
    fig.canvas.draw_idle()  
    fig.canvas.flush_events()
#--------------Parameters-----------------------------------------------------
grid_size=10                                        #Create a grid of size grid_size
density=.20                                          #Minimal board density to store (ie .6=>60/100 nodes visited for 10x10 board) 
data_values=(.25,.5,1)                                #Values to represent board atributes (current-player,wall,open spot)
num_data=1000                                        #Munimal number of example to collect
file_name="test.txt"                                #file name of data
display=False                                       #Display game as its played
list_of_player=[Open_Dist_Player('r'),              #Initilize the list of players 
                Open_Dist_Player('b')]
#--------------Loop untill untill enough data is collected--------------------
n=0                                                 #initilize number of examples collected to 0
while n < num_data:                                 #Repeat untill enough data collected
    board_states=[]                                 #List to keep track of board states per round
    player_decisions=[]                             #List to keep track of player desisions per round
    
    the_grid = Grid(list_of_player,                 #Create new grid
                    grid_size=grid_size)

    if display:                                     #If display is set to true plot the grid 
        fig = the_grid.display_the_grid()           #Display stuff
        plt.ion()                                   #Display stuff
        the_grid.display_the_grid(fig=fig)          #Display stuff
        plot_grid(fig)                              #Display stuff
        
    while the_grid.active_players.__len__() > 1:    #Loop untill no players remain
        bs_turn=[]                                  #list of board states per player per turn
        for player in the_grid.active_players:      #Iterate through active players
            g=the_grid.get_grid(player.node,        #get board state from perspective of player
                                value=data_values)  #Set board representation      
            bs_turn.append(g)                       #Add board state to bs_turn
        board_states.append(bs_turn)                #Add all board states for the turn
        moves = the_grid.move_players()             #Advance all the players
        player_decisions.append(moves)              #Add all players moves to list of moves
        
        if display:                                 #Display logic if needed
            the_grid.display_the_grid(fig=fig)      #Display stuff
            plot_grid(fig)                          #Display stuff
            fig.show()                              #Display stuff
                       
    if display:                                     #Draw the last moves
        the_grid.display_the_grid(fig=fig)          #Display stuff
        plot_grid(fig)                              #Display stuff
    
#--------------Display/ Track winners data------------------------------------
    if the_grid.active_players.__len__() == 0:      #No Winner
        if display:                                 #If diplaying info
            print("Sorry folks, looks like theres not a winner today.")
    else:                                           #There was a winner               
        if display:
            print("The Winner is " +the_grid.active_players[0].color+" !")
        
        X=[]                                        #Create list to hold of board states
        y=[]                                        #list of desision
        winner = the_grid.active_players[0]         #find winner
        i = list_of_player.index(winner)            #look for the index of the winner
        
        for turn in board_states :                  #Iterate through board states by turn
            X.append(turn[i])                       #Add winners board state to list of board states
        for decision in player_decisions:           #Iterate through desisions per turn
            y.append(decision[i])                   #Add decision to list of desisions
        
        v=round(density*(grid_size**2-2)/2)         #Minimal length list to reach density restrictions
        
        if X.__len__()>v:
            n+=X.__len__()-v                        #Add number of eamples collected from round    
            append_data(file_name,X[v:],y[v:])   #Send Data to text file
    if display:
        print('n: '+str(n))
        plt.close(fig)

if display:
    plt.ioff()


