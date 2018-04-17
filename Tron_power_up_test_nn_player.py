"""
Tron_power_up_test_nn_player.py

Author: Diane Meng and Justin Deterding (adaptation of Tron_power_up.py)

This program runs the specified number of games in which the greedy player plays
the neural net player. The number of wins for each player, and the number of ties,
is output. This information is used to infer the neural net player's ability
relative to the greedy player, on whose information it was trained.

4/16/18 - Ran 5 trials of 1000 games each with look sense input. Here are the results:
    NN wins         Ties            Greedy wins
    -------         ----            -----------
    333             319             348
    335             348             317
    319             367             314
    313             384             303
    304             371             325
    **NN average win rate: 32.08%
    **Greedy average win rate: 32.14%
    The players are effectively equal.
    
Generally speaking, these are the results we would expect the neural net to have,
based on training with the same information the greedy user uses to make its
move decisions.

4/16/18 - Ran 5 trials of 1000 games each with board state input. Here are the results:
    NN wins         Ties            Greedy wins
    -------         ----            -----------
    307             381             312
    338             348             314
    338             345             316
    333             345             322
    329             342             329
    **NN average win rate: 32.90%
    **Greedy average win rate: 31.86%
    Here too, the players are effectively equal.
    These results are more significant, because the neural net is interpreting
    the same raw information that we interpreted for the greedy player.
"""

from Tron import Grid 
from Tron_players import Open_Dist_Player, NN_Player
from matplotlib import pyplot as plt

def play():
    #Create a grid of size grid_size
    grid_size=10
    #Initilize the list of players to play on the grid
    list_of_player=[Open_Dist_Player('r'),NN_Player('b')]#,Open_Dist_Player('g'),Player('c'),
                   # Player('m'),Player('y')]
                   
    #Create grid
    the_grid = Grid(list_of_player,grid_size=grid_size)

    while the_grid.active_players.__len__() > 1:
        the_grid.move_players()
        if the_grid.active_players.__len__()>0:
            n=the_grid.active_players[0].node
            grid_pic=the_grid.get_grid(n)
    #print the winner
    if the_grid.active_players.__len__() == 0:
        #print("Sorry folks, looks like theres not a winner today.")
        return(0,1,0) #(NNPlayer, tie, Greedy player)
    else:
        #print("The Winner is " +the_grid.active_players[0].color+" !")
        if the_grid.active_players[0].color == 'r':
            return (0,0,1)
        else:
            return (1,0,0)

nn_wins= 0
ties = 0
greedy_wins = 0
for x in range (0, 1000):
    nn, tie, greedy = play()
    nn_wins += nn
    ties += tie
    greedy_wins += greedy
print("Tournament totals:\nNN wins: " + str(nn_wins) + "\nTies: " + str(ties) + "\nGreedy wins: " + str(greedy_wins))
