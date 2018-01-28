"""
Classes:
	Node:
	Grid:
	Player:



"""
from random import randint 
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
    def __init__(self,players=[], grid_size=50):
        self.grid=[]                        #Grid of Node objects
        self.players_path =[]               #List of [Player,[x-cord],[y-cord]]
        self.active_players=players         #Players still in the game
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
                
    def move_players(self): #Check if dident move*********
        for player in self.active_players:
            player.move() #Player moves themself to their next node
        for player in self.active_players:
            if player.node == "bnd" or player.node.visited: #Player hit a wall and should be removed from game
                self.defeted_players.append(player)         #Move player to the list of defeted players
                self.active_players.remove(player)          #Remove Player from list of active players
            else:
                player.node.visited=True            #Sets the node the player moved to as visited
                self.add_curr_node_to_path(player)  #Adds node to players current path
                    
    def add_curr_node_to_path(self,player):
        for a_player in self.players_path:
            if a_player[0] is player:
                a_player[1].append(player.node.cordinate[0])
                a_player[2].append(player.node.cordinate[0])
     
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
    grid=Grid()     #Blank grid, needs to be replaced with real grid
    
    def __init_(self,color):
        self.node=None
        self.color=color
    
    #def possible_Move()    
    
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
        else:
            i = randint(0,pos_moves.__len__()-1)
            self.directional_move(pos_moves[i])
        return
            
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
        if   direction == "left" : self.node=self.node.left
        elif direction == "right": self.node=self.node.right
        elif direction == "up"   : self.node=self.node.up
        elif direction == "down" : self.node=self.node.down
    