"""
Classes:
	Node:
	Grid:
	Player:



"""
from random import randint 
#------------------------------Node-------------------------------------------
class Node:
    def __init__(self, visited=False):
        self.visited=visited #Boolean has the node been visited
        self.left='bnd'
        self.right='bnd'
        self.up='bnd'
        self.down='bnd'

    #Recursively iterate down or to the right to determine node location
	#in the grid
    def x_cord(self, x=0):
        if self.left != "bnd": x = self.left.x_cord(x+1)
        return x
    def y_cord(self, y=0):
        if self.down != "bnd": y = self.down.y_cord(y+1)
        return y
         
#------------------------Grid-------------------------------------------------
class Grid:          
    def __init__(self,players, grid_size=50):
        self.generate_grid(grid_size) 	#build the self.grid attribute
        self.set_players(players)		#build the self.players_path attribute
        self.active_players=players     #Players still in the game
        self.defeted_players=[] 		#Defeted players
        
    def set_players(self, players): 
        self.players_path=[]
        for player in players:
            self.players_path.append([player,[],[]])
        #set the start node of the players
        grid_size = self.grid.__len__()
        for player in players:
            x= randint(0, grid_size-1); y= randint(0, grid_size-1)
            while self.grid[x][y].visited:
                x= randint(0, grid_size-1); y= randint(0, grid_size-1)    
            player.node=self.grid[x][y]
            self.add_curr_node_to_path(player)
            self.grid[x][y].visited=True
        
    def generate_grid(self,grid_size):
        self.grid=[]
        for x in range(grid_size):
            self.grid.append([])  
            for y in range(grid_size):
                self.grid[x].append(Node())
                if y == 0: # At the bottom most row of the grid 
                    self.grid[x][y].down= "bnd"
                else: #set down of the current node and the up of the previous node
                    self.grid[x][y].down = self.grid[x][y-1]
                    self.grid[x][y-1].up = self.grid[x][y]
                if x == 0: # at the left most collum of grid 
                    self.grid[x][y].left = "bnd"
                else: #set the left of the current node and the right of the previous node
                    self.grid[x][y].left = self.grid[x-1][y]
                    self.grid[x-1][y].right = self.grid[x][y]    
                if y == grid_size-1: # At the top of the grid 
                    self.grid[x][y].up = "bnd"
                if x == grid_size-1: # At right most collum of the grid
                    self.grid[x][y].right = "bnd"
                
    def move_players(self):#Mutual destruction
        for player in self.active_players:
            player.move() #Player moves themself to their next node
            if player.node == "bnd" or player.node.visited: #Player hit a wall and should be removed from game
                self.defeted_players.append(player)
                self.active_players.remove(player)
            else:
                player.node.visited=True
                self.add_curr_node_to_path(player)
                
    def add_curr_node_to_path(self,player):
        for a_player in self.players_path:
            if a_player[0] is player:
                a_player[1].append(player.node.x_cord())
                a_player[2].append(player.node.y_cord())
     
    def display_the_grid(self,fig=None,ax=None, paths = []):
        ###ANIMATION???###
        for x in self.grid:
           for y in x:
               if y.visited:print('X ',end='')
               else: print("0 ",end='')
           print()        
        print("------------------------")
                
#-------------------------Player----------------------------------------------
class Player:
    #Class variable all instances of player shair the same grid
    grid="Grid Not Established"
    
    def __init_(self,color):
        #Individual payer variable
        self.node=None
        self.color=color
        
    #This method should be overidden by a sub class to impliment a "Smart move"
    def move(self): 
        pos_moves=[]
        if self.node.left!="bnd" and not(self.node.left.visited):
            pos_moves.append("left")
        if self.node.right!="bnd" and not(self.node.right.visited):
            pos_moves.append("right")
        if self.node.up!="bnd" and not(self.node.up.visited): 
            pos_moves.append("up")
        if self.node.down!="bnd" and not(self.node.down.visited): 
            pos_moves.append("down")
        if pos_moves.__len__()==0:
            self.directional_move("up")
        else:
            i = randint(0,pos_moves.__len__()-1)
            self.directional_move(pos_moves[i])
            
    def directional_move(self,direction):
        #Move the player
        if   direction == "left" : self.node=self.node.left
        elif direction == "right": self.node=self.node.right
        elif direction == "up"   : self.node=self.node.up
        elif direction == "down" : self.node=self.node.down
    