
import random
from tkinter import *
import time

#-----------------------------------    

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

#-----------------------------------    

class GameObject:
    
    def __init__(self, pos):
        self.position = Vector(pos[0], pos[1])
    
    def isCollidingWith(self, otherGameObject):  # Checks collosion between itself
        #############################            #   and another game object. Returns
        #   INSERT YOUR CODE HERE                #   True if they are colliding,
        pass
        	                                    #   False otherwise.
        #############################
    
    def Draw(self):                    # This function MUST be overidden by all 
        raise                          #   sub-classes !!!
        

#-----------------------------------

class Background(GameObject):
    def __init__(self):
        #############################
        #   INSERT YOUR CODE HERE
        self.img = PhotoImage(file="assets/bg.gif")
        #############################
    
    def Draw(self):
        #############################
        #   INSERT YOUR CODE HERE
        Game.canvas.create_image(320,240, image=self.img)
        #############################
        
#-----------------------------------
    
class Brick(GameObject):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self):
    	pass
    	
    #############################


class NormalBrick(Brick):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self):
    	self.img = PhotoImage(file="assets/normalbrick.gif")
    	self.collision=False
    	self.b=[] #contains id of bricks to be deleted
    	self.Nid=[]
    	self.collision_count=0	
    def Draw(self):
    	self.Nid=[]
    	self.x=85
    	for _ in range(8):
    		self.NormalBrick_id=Game.canvas.create_image(self.x,100,image=self.img)
    		self.x+=70
    		self.Nid.append(self.NormalBrick_id)
    	self.x=85
    	for _ in range(8):
    		self.NormalBrick_id=Game.canvas.create_image(self.x,135,image=self.img)
    		self.x+=70
    		self.Nid.append(self.NormalBrick_id)
    	
    	# When Ball hits the brick #
    	if self.collision==True:
    		for n in range(len(self.b)-1):			
    			Game.canvas.delete(self.Nid[self.b[n]])   	
   			   	   	   				   				 	
    #############################
    
class MetalBrick(Brick):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self):
    	self.img = PhotoImage(file="assets/metalbrick.gif")
    	self.Mid=[]
    	self.collision=False
    	self.c=[] #contains id of bricks to be deleted
    	self.collision_count=0
    def Draw(self):
    	self.Mid=[]
    	self.x=85
    	for _ in range(8):
    		self.MetalBrick_id=Game.canvas.create_image(self.x,65,image=self.img)
    		self.x+=70
    		self.Mid.append(self.MetalBrick_id)
    	if self.collision==True:
    		for n in range(len(self.c)-1):
    			Game.canvas.delete(self.Mid[self.c[n]])   			

    #############################

class GlassBrick(Brick):

	def __init__(self):
		self.img = PhotoImage(file="assets/glassbrick.gif")
		self.Gid=[]		
		self.collision=False
		self.a=[] #contains id of bricks to be deleted
	def Draw(self):	
		self.Gid=[]
		self.x=85
		
		for _ in range(8):
			self.GlassBrick_id=Game.canvas.create_image(self.x,170,image=self.img)
			self.x+=70
			self.Gid.append(self.GlassBrick_id)
		# When Ball hits the brick #
		if self.collision==True:
			for n in range(len(self.a)-1):		
				Game.canvas.delete(self.Gid[self.a[n]])

								
class ExplodingBrick(Brick):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self):
    	self.img=PhotoImage(file="assets/explodingbrick.gif")
    	self.collision=False
    	self.Eid=[]
    	self.pos=[(85,170),(225,65),(155,100),(365,135),(225,170),(225,100),(295,170),(365,65)]
    	self.lis=[]
    	self.d=[]
    	for _ in range(3):
    		self.rand=random.randrange(0,8)
    		self.lis.append(self.rand)    	
    def Draw(self):
    	self.Eid=[]
    	self.x=0
    	self.y=0
    	
    	for _ in range(3):
    		self.ExplodingBrick_id=Game.canvas.create_image(self.pos[self.lis[self.x]][0],self.pos[self.lis[self.y]][1],image=self.img)
    		self.Eid.append(self.ExplodingBrick_id)
    		self.x+=1
    		self.y+=1
    	if self.collision==True:
    		for n in range(len(self.d)-1):
    			Game.canvas.delete(self.Eid[self.d[n]])
   	
    #############################


#-----------------------------------
    
class Ball(GameObject):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self, game, pos, vel):
    	

    	GameObject.__init__(self, pos) # Call the super class constructor
    	self.velocity = Vector(vel[0], vel[1]) # add velocity
    	self.game = game # reference to the game object
    	self.img = PhotoImage(file="assets/ballBlue.png") # player image
    	self.y=3.5
    	self.x=0
    	self.Ball_pos=[320.0,240.0]
    def Draw(self):
    	    	
    	self.Ball_id=Game.canvas.create_image(self.position.x,self.position.y, image=self.img)
    	self.Ball_pos=Game.canvas.coords(self.Ball_id) #Current position of the Ball
    	   	
    	if (self.Ball_pos[0]-self.img.width()//2)<=0: #x boundary
    		self.x=3
    	if (self.Ball_pos[0]+self.img.width()//2)>=640:
    		self.x=-3    		
    	
    #############################

    
#-----------------------------------

class Powerup(GameObject):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self,pos):
    	GameObject.__init__(self, pos)
    #############################

    
class Life(Powerup):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self,game,pos,vel):
    	Powerup.__init__(self,pos)
    	self.img = PhotoImage(file="assets/life.gif")
    	self.velocity = Vector(vel[0], vel[1]) # add velocity
    	self.game = game # reference to the game object   	
    def Draw(self):
    	self.Life_id=Game.canvas.create_image(self.position.x,self.position.y, image=self.img)
    	self.position.y+=2
    	    	
    #############################

    
class FastPaddle(Powerup):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self,game,pos,vel):
    	Powerup.__init__(self,pos)
    	self.img = PhotoImage(file="assets/fastpaddle.gif")
    	self.velocity = Vector(vel[0], vel[1]) # add velocity
    	self.game = game # reference to the game object
    def Draw(self):
    	self.FastPaddle_id=Game.canvas.create_image(self.position.x,self.position.y, image=self.img)
    	self.position.y+=2


    #############################


class CrazyBall(Powerup):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self,game,pos,vel):
    	Powerup.__init__(self,pos)
    	self.img = PhotoImage(file="assets/crazyball.gif")
    	self.velocity = Vector(vel[0], vel[1]) # add velocity
    	self.game = game # reference to the game object
    def Draw(self):
    	self.CrazyBall_id=Game.canvas.create_image(self.position.x,self.position.y, image=self.img)
    	self.position.y+=2

    #############################

#-----------------------------------

class Player(GameObject):
    def __init__(self, game, pos, vel):
        #############################
        #   INSERT YOUR CODE HERE
        GameObject.__init__(self, pos) # Call the super class constructor
        self.velocity = Vector(vel[0], vel[1]) # add velocity
        self.game = game # reference to the game object
        self.img = PhotoImage(file="assets/paddleBlu.gif") # player image
        self.Paddle_Pos=[320.0,420.0]
        
        #############################

    def Draw(self):
        #############################
        #   INSERT YOUR CODE HERE
        self.Paddle_id=Game.canvas.create_image(self.position.x,self.position.y, image=self.img)
        self.Paddle_Pos=Game.canvas.coords(self.Paddle_id) #Current position of the Paddle
        if self.Paddle_Pos[0]<=50:  #Paddle remains within the boundaries of the Window
        	self.position.x=50
        elif self.Paddle_Pos[0]>=590:
        	self.position.x=590
               
        #############################
   
#-----------------------------------

class Game:
    canvas = None
    def __init__(self, canvas):
        Game.canvas = canvas           # Save canvas for future use
        self.gameObjects = []
        self.Powerups=[]
        self.counter=0          # A list of ALL game objects in the game
    
        #############################
        #   INSERT YOUR CODE HERE
        self.Background = Background()
        
        self.player = Player(self, (320, 420), (0,0)) # Our Hero
        self.Ball=Ball(self,(320,240),(0,0))
        self.NormalBrick=NormalBrick()
        self.MetalBrick=MetalBrick()
        self.GlassBrick=GlassBrick()
        self.Life=Life(self,(320,60),(0,0))
        self.FastPaddle=FastPaddle(self,(320,60),(0,0))
        self.CrazyBall=CrazyBall(self,(320,60),(0,0))
        #self.ExplodingBrick=ExplodingBrick()
        self.gameObjects.append(self.Background)
        self.gameObjects.append(self.MetalBrick)
        self.gameObjects.append(self.NormalBrick)
        self.gameObjects.append(self.GlassBrick)
        #self.gameObjects.append(self.ExplodingBrick)
        self.gameObjects.append(self.player)
        self.gameObjects.append(self.Ball)
        self.Powerups.append(self.Life)
        self.Powerups.append(self.FastPaddle)
        self.Powerups.append(self.CrazyBall)       
        self.lives=2
        self.Score=0 
        self.powerTime=False
        self.Paddle_speed=10
        self.Ball_speed=4
        self.win=False
        random.shuffle(self.Powerups)    

        #############################

    def Draw(self):                    # This function draws ALL of the things
        Game.canvas.delete(ALL)        # First clear the screen
        for obj in self.gameObjects:   # Now the objects draw THEMSELVES one by one
            obj.Draw()
        if self.counter==20 and self.Powerups!=[]:
        	self.powerTime=True
        	
        if self.powerTime==True and self.Powerups!=[]:
        	self.Powerups[0].Draw()
   
        self.life_label=Game.canvas.create_text(50,20,text='Lives: %d'%(self.lives),fill='white',font=('Times',18)) 
        self.score_label=Game.canvas.create_text(300,20,text='Score: %d'%(self.Score),fill='white',font=('Times',18))
        if self.lives==0:
        	Game.canvas.create_text(320,240,text='Game Over',fill='white',font=('Times',30))
        	self.Ball.x=0
        	self.Ball.y=0
        	Game.canvas.delete(self.Ball.Ball_id)
        if self.win==True:
        	Game.canvas.create_text(320,240,text='YOU WIN!',fill='white',font=('Times',30))
           
    def LeftKeyPressed(self):        
        #############################
        #   INSERT YOUR CODE HERE
        self.player.position.x-=self.Paddle_speed
        #############################
   
    def RightKeyPressed(self):        
        #############################
        #   INSERT YOUR CODE HERE
        self.player.position.x+=self.Paddle_speed
        #############################
            
    def Update(self):                  
        #############################
        #   INSERT YOUR CODE HERE
        
                  
        self.Ball.position.y+=self.Ball.y 
        self.Ball.position.x+=self.Ball.x
               
        #Ball stays within the boundaries of window
        if (self.Ball.Ball_pos[1]-self.Ball.img.height()//2)<=0:
        	self.Ball.y=self.Ball_speed
        if (self.Ball.Ball_pos[1]+self.Ball.img.height()//2)>=480: #y boundary
        	self.Ball.velocity.y=0
        	self.Ball.velocity.x=0
        	self.Ball.x=0
        	self.Ball.position.x=320
        	self.Ball.position.y=240
        	self.player.position.x=320
        	time.sleep(0.5)
        	self.lives-=1
        
        #Paddle and Ball collision
        if self.Ball.Ball_pos[0]>=(self.player.Paddle_Pos[0]-self.player.img.width()//2) and (self.Ball.Ball_pos[0])<=(self.player.Paddle_Pos[0]+self.player.img.width()//2): #checking Ball with left and right side of the paddle
        	if self.Ball.Ball_pos[1]>=(self.player.Paddle_Pos[1]-self.player.img.height()): #checking y axis of the ball with upper y axis of paddle
        		self.Ball.y=-self.Ball_speed

        #Ball movement
        		if self.Ball.Ball_pos[0]==self.player.Paddle_Pos[0]: #Ball hits centre of the Paddle
        			self.Ball.x=0
        		if self.Ball.Ball_pos[0]>(self.player.Paddle_Pos[0]): #Ball hits right side of Paddle
        			self.Ball.x=3
        		if self.Ball.Ball_pos[0]<(self.player.Paddle_Pos[0]): #Ball hits left side of Paddle
        			self.Ball.x=-3
        #Ball Glass Brick Collision
        for a in range(8):
        	try:
        		self.GlassPos=Game.canvas.coords(self.GlassBrick.Gid[a]) 
        		if self.Ball.Ball_pos[0]>=(self.GlassPos[0]-self.GlassBrick.img.width()//2) and (self.Ball.Ball_pos[0])<=(self.GlassPos[0]+self.GlassBrick.img.width()//2):
        			if self.Ball.Ball_pos[1]<=(self.GlassPos[1]+self.GlassBrick.img.height()):
        				self.Ball.y=self.Ball_speed 
        				self.GlassBrick.collision=True
        				self.GlassBrick.a.append(a)
        				self.Score+=50
 			
        	except IndexError:
        		pass
        #Ball NormalBrick collission#
        for b in range(16):
        	try:
        		self.NormalPos=Game.canvas.coords(self.NormalBrick.Nid[b]) #current pos of normal brick
        		if self.Ball.Ball_pos[0]>=(self.NormalPos[0]-self.NormalBrick.img.width()//2) and (self.Ball.Ball_pos[0])<=(self.NormalPos[0]+self.NormalBrick.img.width()//2):
        			if self.Ball.Ball_pos[1]<=(self.NormalPos[1]+self.NormalBrick.img.height()):
        				self.Ball.y=self.Ball_speed       				
        				self.NormalBrick.collision_count+=1
        				if self.NormalBrick.collision_count>2:
        					self.NormalBrick.collision=True
        					self.NormalBrick.b.append(b)
        					self.NormalBrick.collision_count=0
        					self.Score+=100        					      				
        	except IndexError:
        		pass
        #Ball MetalBrick collission#
        for c in range(8):
        	try:
        		self.MetalPos=Game.canvas.coords(self.MetalBrick.Mid[c]) #current pos of metal brick
        		if self.Ball.Ball_pos[0]>=(self.MetalPos[0]-self.MetalBrick.img.width()//2) and (self.Ball.Ball_pos[0])<=(self.MetalPos[0]+self.MetalBrick.img.width()//2):
        			if self.Ball.Ball_pos[1]<=(self.MetalPos[1]+self.MetalBrick.img.height()):
        				self.Ball.y=self.Ball_speed
        				self.MetalBrick.collision_count+=1
        				if self.MetalBrick.collision_count>7: 
        					self.MetalBrick.collision=True
        					self.MetalBrick.c.append(c)
        					self.MetalBrick.collision_count=0
        					self.Score+=200   
        	except IndexError:
        		pass

        #Ball Life Collission#
        if self.Life.position.x>=(self.player.Paddle_Pos[0]-self.player.img.width()//2) and (self.Life.position.x)<=(self.player.Paddle_Pos[0]+self.player.img.width()//2): #checking x axis
        	if self.Life.position.y>=(self.player.Paddle_Pos[1]-self.player.img.height()) and self.Life.position.y<=(self.player.Paddle_Pos[1]+self.player.img.height()): #checking y axis 
        		if self.Life in self.Powerups:
        			self.Powerups.remove(self.Life)
        			self.powerTime=False
        			self.Life.position.y-=4
        			self.lives+=1
        			self.counter=0        
        #Ball FastPaddle Collission#
        if self.FastPaddle.position.x>=(self.player.Paddle_Pos[0]-self.player.img.width()//2) and (self.FastPaddle.position.x)<=(self.player.Paddle_Pos[0]+self.player.img.width()//2): #checking x axis
        	if self.FastPaddle.position.y>=(self.player.Paddle_Pos[1]-self.player.img.height()) and self.FastPaddle.position.y<=(self.player.Paddle_Pos[1]+self.player.img.height()): #checking y axis 
        		if self.FastPaddle in self.Powerups:
        			self.Powerups.remove(self.FastPaddle)
        			self.powerTime=False
        		self.FastPaddle.position.y-=4
        		self.counter=0
        		self.Paddle_speed=20
        if self.counter==5:
        	self.Paddle_speed=10
        #Ball CrazyBall Collission#
        if self.CrazyBall.position.x>=(self.player.Paddle_Pos[0]-self.player.img.width()//2) and (self.CrazyBall.position.x)<=(self.player.Paddle_Pos[0]+self.player.img.width()//2): #checking x axis
        	if self.CrazyBall.position.y>=(self.player.Paddle_Pos[1]-self.player.img.height()) and self.CrazyBall.position.y<=(self.player.Paddle_Pos[1]+self.player.img.height()): #checking y axis  #checking y axis 
        		if self.CrazyBall in self.Powerups:
        			self.Powerups.remove(self.CrazyBall)
        			self.powerTime=False
        		self.CrazyBall.position.y-=4
        		self.counter=0
        		self.Ball_speed=8
        if self.counter==5:
        	self.Ball_speed=4

        #############################
            
#-----------------------------------
class GameWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("Project 2 -- Breakout Game")
        self.root.geometry('640x480')

        self.canvas = Canvas(self.root, width = 640, height = 480)
        self.canvas.grid(column=0, row=0)
        self.canvas.after(1, self.OneSecTimer)
        self.canvas.bind("<Key>", self.KeyPressed)
        self.canvas.focus_set()
        
        self.game = Game(self.canvas)    
        self.root.after(1, self.GameLoop)
        self.root.mainloop()
    
    def KeyPressed(self, event):
        c = str(event.char)
        if c == 'a':
            self.game.LeftKeyPressed()
        if c == 'd':
            self.game.RightKeyPressed()

    
    def GameLoop(self):        
        self.game.Update()
        self.game.Draw()
        
        self.root.after(1000//80, self.GameLoop)

    def OneSecTimer(self):
        print("One second Tick")
        self.canvas.after(1000, self.OneSecTimer)
        self.game.counter+=1
        

        
#-----------------------------------


game = GameWindow()

