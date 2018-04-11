"""
Classes:
	Node:
	Grid:
	Player:



"""
from random import randint 
from matplotlib import pyplot as plt
import numpy as np
#------------------------------Node-------------------------------------------
class Node:
    """
    ->The Node object gives the Grid linked list style data structure. 
    ->Each Node has a referance to its naboring nodes (left,right,up, down) 
    unless at a boundry when the referance is a string "bnd"
    ->Visited is true if the node has been visited by a player
    ->Cordinate is the [x,y] cordinate of the Node in the grid.
    """
    def __init__(self,cordinate=[], visited=False, left='bnd', right='bnd',
                 up='bnd', down='bnd'):
        self.visited=visited       	#Boolean has the node been visited
        self.cordinate=cordinate   #[x-Cordinate,y-Cordinate]
        self.left=left			           #Referance to the left node
        self.right=right		         #Referance to the right node
        self.up=up 			             #Referance to the up node
        self.down=down           		#Referance to the down node
         
#------------------------Grid-------------------------------------------------
class Grid:          
    def __init__(self,players=[], grid_size=1):
        self.grid=[]                        #Grid of Node objects
        self.players_path =[]               #List of [Player,[x-cord],[y-cord]]
        self.active_players=players.copy()  #Players still in the game
        for player in self.active_players:  #Set this grid as the grid of all the players
            player.grid=self                #Set players grid
        self.defeted_players=[] 		          #Defeted players
        self.generate_grid(grid_size) 	     #build the self.grid attribute
        self.set_players(players)		         #build the self.players_path attribute
        
    def set_players(self, players): 
        if players.__len__()>1:
            players[0].grid=self            #Set the Player grid parameter to this grid
        for player in players:              #Structure of the players path Variabel
            self.players_path.append([player,[],[]])
        grid_size = self.grid.__len__()     #set the start node of the players
        for player in players:
            x= randint(0, grid_size-1)      #Randomaly assign start x-location 
            y= randint(0, grid_size-1)      #Randomaly assign start y-location
            while self.grid[x][y].visited:  #Check that Randomly asigned position has
                x= randint(0, grid_size-1)  #not previously assigned a player
                y= randint(0, grid_size-1)    
            player.node=self.grid[x][y]     #Set Players Node attribute
            self.add_curr_node_to_path(player) #And starting location to path
            self.grid[x][y].visited=True    #Set node visited attribute to True
        return
        
    def get_grid(self,current_node,value=(1,.5,0)):
        """
        get_grid returns a list representation of the grid, where different atributes of the grid
        are represented by a value (self,wall,open_space)
        """
        grid_list=[]
        for row in self.grid:                       #iterate through rows in grid
            for col in row:                         #itereate through nides in a row
                if col.visited:                     
                    if col is current_node:
                        grid_list.append(value[0])  #If current node is self add value[0] 
                        
                    else:
                        grid_list.append(value[1])  #If current node is visted add value[1]
                else:
                    grid_list.append(value[2])      #if current node is open add value[2]
        return grid_list
    
    def generate_grid(self,grid_size):
        for x in range(grid_size):
            self.grid.append([])  
            for y in range(grid_size):
                self.grid[x].append(Node(cordinate=[x,y]))
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
        return
                
    def move_players(self, display= False): 
        moves = [] #List of players moves
        #Step 1 Move all the active players
        for player in self.active_players:
            moves.append(player.move()) #Player moves themself to their next node
        #Step 2 Remove players that hit an obstical in their move
        players_to_remove=[]
        for player in self.active_players: #Traverse all the active players
            #Checks 1 and 2 Check for simple collision.
            if player.node == "bnd": #Check 2-----------hit a boundry---------
                players_to_remove.append(player)
                if display:
                    print("Cause of death of Player " +player.color+": Player hit a boundry")
            elif player.node.visited: #Check 1--------------hit a wall--------
               players_to_remove.append(player)
               self.add_curr_node_to_path(player)          #Adds node to players current path
               if display:
                   print("Cause of death of Player " +player.color+": Player hit a wall")
            else:
                #Checks 3 & 4 iterative checks for mutual collisions or stalls
                for other_player in self.active_players: #check if there was a mutual collision.
                    if other_player.node is player.node and other_player is not player and player not in players_to_remove:
                        players_to_remove.append(player)
                        self.add_curr_node_to_path(player)          #Adds node to players current path
                        if display:
                            print("Cause of death of Player " +player.color+" : Mutual Collision")
                for prev_player in self.players_path: # check that player has move
                    if prev_player[0] is player:
                        if [prev_player[1][-1],prev_player[2][-1]]==player.node.cordinate and player not in players_to_remove:
                            self.defeted_players.append(player)         #Move player to the list of defeted players
                            players_to_remove.append(player)
                            if display:
                                print("Cause of death of Player " +player.color+": Player dident move")
                #Player Survived
                if player not in players_to_remove:
                    player.node.visited=True            #Sets the node the player moved to as visited
                    self.add_curr_node_to_path(player)  #Adds node to players current path
        #Remove players
        for player_to_remove in players_to_remove:
            self.defeted_players.append(player_to_remove)
            self.active_players.remove(player_to_remove)
            if not isinstance(player.node, str): 
                player.node.visited=True #If mutual collision need to set to true
        
        return moves
                    
    def add_curr_node_to_path(self,player):
        for a_player in self.players_path:
            if a_player[0] is player:
                a_player[1].append(player.node.cordinate[0])
                a_player[2].append(player.node.cordinate[1])
        return
     
    def display_the_grid(self,fig=None):
        #Initilization-------------------------------------------
        if fig == None: #if no figure has been create figure
            fig = plt.figure()
        if fig.axes.__len__() == 0: # if no axies create axes
            fig.add_axes(plt.axes(xlim=(-.5,self.grid.__len__()-1+.5)
                                 ,ylim=(-.5,self.grid.__len__()-1+.5)))
            ax= fig.gca()
            ax.set_xticks(np.arange(0, self.grid.__len__(), self.grid.__len__()/10),minor=False)
            ax.set_yticks(np.arange(0, self.grid.__len__(), self.grid.__len__()/10),minor=False)
            ax.set_xticks(np.arange(0, self.grid.__len__(), 1),minor=True)
            ax.set_yticks(np.arange(0, self.grid.__len__(), 1),minor=True)
            plt.grid(which='both')
        if fig.axes[0].lines.__len__() == 0: # if no lines create lines
            for player in self.players_path:
                fig.axes[0].plot(player[1],player[2],player[0].color)#player=[player object,x_cor,y_cord]
            
            fig.axes[0].plot([-.25,-.25,self.grid.__len__()-1+.25,self.grid.__len__()-1+.25,-.25],
                             [-.25,self.grid.__len__()-1+.25,self.grid.__len__()-1+.25,-.25,-.25],'k') #Plot an actual boundry
        #End Initilization------------------------------------------
        else:
            for i in range(self.players_path.__len__()):
                player = self.players_path[i]
                fig.axes[0].lines[i].set_xdata(player[1])
                fig.axes[0].lines[i].set_ydata(player[2])
        return fig
                
#-------------------------Player----------------------------------------------
class Player:
    """ 
    -> Player class should be overode, to impliment an inteligent move.
    -> Attributes:
        +grid: This attribute is set by the Grid when the players are passed 
            to the grid to start the game. All players have access to a 
            referance of the same grid.
        +node: This is the node that the player exist at.
        +color: Players identifying color for animation and player 
            identification.
    """
    
    
    
    def __init__(self,color='r'):
        self.node=None
        self.color=color
        self.grid=Grid()
        
    """
    look_sence documentation:
        add in if it was a 'bnd', player or wall
    """
    def look_sense(self,direction='all'):    
        if direction == 'left':#--------------LEFT----------------------------
            l_node=self.node.left
            l_count=0
            while not l_node == 'bnd' and not l_node.visited:
                l_count+=1
                l_node=l_node.left
            if l_node == "bnd":
                return [direction,l_count,"bnd"]
            else:
                for player in self.grid.active_players:
                    if player.node is l_node:
                        return [direction,l_count,"player"]
                return [direction,l_count,"wall"]
        elif direction == 'right':#-------------RIGHT-------------------------
            r_node=self.node.right
            r_count=0
            while not r_node == 'bnd' and not r_node.visited:
                r_count+=1
                r_node=r_node.right
            if r_node == "bnd":
                return [direction,r_count,"bnd"]
            else:
                for player in self.grid.active_players:
                    if player.node is r_node:
                        return [direction,r_count,"player"]
                return [direction,r_count,"wall"]
        elif direction == 'up':#--------------UP------------------------------
            u_node=self.node.up
            u_count=0
            while not u_node == 'bnd' and not u_node.visited:
                u_count+=1
                u_node=u_node.up
            if u_node == "bnd":
                return [direction,u_count,"bnd"]
            else:
                for player in self.grid.active_players:
                    if player.node is u_node:
                        return [direction,u_count,"player"]
                return [direction,u_count,"wall"]
        elif direction == 'down':#--------------DOWN-------------------------
            d_node=self.node.down
            d_count=0
            while not d_node == 'bnd' and not d_node.visited :
                d_count+=1
                d_node=d_node.down
            if d_node == "bnd":
                return [direction,d_count,"bnd"]
            else:
                for player in self.grid.active_players:
                    if player.node is d_node:
                        return [direction,d_count,"player"]
                return [direction,d_count,"wall"]
        elif direction == 'all':#--------------ALL----------------------------
            left = self.look_sense('left')
            right = self.look_sense('right')
            up = self.look_sense('up')
            down = self.look_sense('down')
            return [left,right,up,down]
        else:
            return []
            
    def move(self): 
        """
        ->The basic move implimented, chooses directions semi-randomly. It 
          only picks randomly from directions it know wont destroy it, untill 
          its cornered.
        ->The move method is used by the grid to move the player.
        ->The move method should requier no inputs and it souldn't return 
          anything instead when your "AI/Algorithum" determines which 
          direction it wants to move (left, right, up, down) it should call 
          the directional_move method and enter which move it would like the 
          player to take.
        """
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
        i = randint(0,pos_moves.__len__()-1)   
        return self.directional_move(pos_moves[i])
            
    def directional_move(self,direction):
        """
        ->directional_move will set your players new node. Afterwhich the grid
          will determine if this is a valid move.
        ->Below are the possible moves and a cordinate and diagram 
          representation of what each command does.
          Let; (xi,yi) be the inital cordinates of the player
               (xf,yf) be the cordinates after the move.
          "left"  => Move decrease along the x-axis => xf=xi-1 
          "right" => Move increase along the x-axis => xf=xi+1 
          "up"    => Move increase along the y-axis => yf=yi+1 
          "down"  => Move decrease along the y-axis => yf=yi-1 
        Y
        ^          "up"
        |            ^
        |            |
        |   "left" <-o-> "right"
        |            |
        |         "down"
        |
        -------------------> X
        """
        if   direction == "left" : 
            self.node=self.node.left
            return [1,0,0,0]
        elif direction == "right": 
            self.node=self.node.right
            return [0,1,0,0]
        elif direction == "up"   : 
            self.node=self.node.up
            return [0,0,1,0]
        elif direction == "down" : 
            self.node=self.node.down
            return [0,0,0,1]
    