#sys is a modul to acces some functionality in your system
import pygame, sys, random

#----------------------------------Animation phase----------------------------------

def ball_animation():
	#global enable us to acces glopbal scope 
	global ball_speed_x, ball_speed_y
	
	# moving the ball every frame  by the ball spped we defind x=7 and y=7
	# NB ball.x where x is the object ball = pygame.Rect(screen_width/2-15,screen_height/2-15, 30, 30)
	ball.x += ball_speed_x
	ball.y += ball_speed_y

	# crate a boundry 
	if ball.top <= 0 or ball.bottom >= screen_height:
		#reverse the horizontal ball speed hence ball_speed_y = -7
		ball_speed_y *= -1
	if ball.left <= 0 or ball.right >= screen_width:
		#reverse the horizontal ball speed hence ball_speed_x = -7
		#ball_speed_x *= -1
		#----------------------------------Resart ball phase----------------------------------
		ball_start()
		#----------------------------------Resart ball phase----------------------------------
		# --Rec1.colliderect(Rec2) --Returns true if any portion of either rectangle(rec1 and rec2) overlap or touches them self
	if ball.colliderect(player) or ball.colliderect(opponent):
		ball_speed_x *= -1
		
#----------------------------------Animation phase----------------------------------

#----------------------------------Input phase----------------------------------
def player_animation():
	player.y += player_speed

	#the logic below avoid the player to move out side of the window or the surface
	# if the player top is less than zero, place the player top at position zero
	if player.top <= 0:
		player.top = 0

	# if the player bottom is greather sceen hight, place the player bottom at position sceen hight	
	if player.bottom >= screen_height:
		player.bottom = screen_height
		
#----------------------------------Input phase----------------------------------


#----------------------------------Opponont phase----------------------------------
def opponent_ai():
	 #5 opponent logic
     #if the opponent top is above the center of the ball  : move the oppenet down
     #if the bottom opponent the opponent is below the center of the ball : move the component up
    #the speed of the opponent will be use to determine the difficulty   

	if opponent.top < ball.y:
		opponent.y += opponent_speed
	if opponent.bottom > ball.y:
		opponent.y -= opponent_speed

	#5 opponent logic to void it to go out from the window
	if opponent.top <= 0:
		opponent.top = 0
	if opponent.bottom >= screen_height:
		opponent.bottom = screen_height		
#----------------------------------Opponont phase----------------------------------

#----------------------------------Resart ball phase----------------------------------
def ball_start():
	global ball_speed_x, ball_speed_y

	#make ball appriear in center
	ball.center = (screen_width/2, screen_height/2)
	#The choice() method returns a randomly selected element from string, a range, a list, a tuple etc
	ball_speed_y *= random.choice((1,-1))
	ball_speed_x *= random.choice((1,-1))
#----------------------------------Resart ball phase----------------------------------	

# General setup
#--pygame.init()-- initiate the pygame module. all ways need for any pygame code
pygame.init()

#--pygame.time.Clock()--This function is used to create a clock object which can be used to keep track of time. 
#---------The various methods of clock object are below:----------
#tick():This method should be called once per frame. It will compute how many milliseconds have passed since the
#  previous call. If you pass the optional framerate argument the function will delay to keep the game running slower
#  than the given ticks per second. For example if we pass 10 as argument the program will never run at more than 10
#  frames per second.
#get_time():It is used to obtain a number of milliseconds used between two tick().
#get_fps():it gives information regarding the clock frame rate. it returns the output in floating-point value.
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280 #pixel wide
screen_height = 960 #pixel hight
#--display.set_mode((screen_width,screen_height))-- return a display surface object or your window
screen = pygame.display.set_mode((screen_width,screen_height))

#--pygame.display.set_caption('Pong')-- given the window or sreen a title
pygame.display.set_caption('Pong')



#----------------------------------Drawing phase----------------------------------

# Colors
# defind your on color as (R,G,B)
light_grey = (200,200,200)

	#----------------------------------Animation phase----------------------------------
	# defind speed variable require for the movent of the ball
		# Game Variables
ball_speed_x = 7
ball_speed_y = 7
	#----------------------------------Animation phase----------------------------------

	#----------------------------------input phase----------------------------------
	# defind speed variable require for the movent of players
player_speed = 0	
player_speed = 0
	#----------------------------------input phase----------------------------------
    #----------------------------------Opponont phase----------------------------------
	# defind speed variable require for the opponent movent speed
opponent_speed = 7
	#----------------------------------Opponont phase----------------------------------

#--pygame.Color('colorNameOnline ')-- use to create color
bg_color = pygame.Color('grey12')

# Game Rectangles
#pygame.Rect(x(lesft),y(top),width,height)
					
			#- ...					
			#-2
			#-1
#-..,-2,-1,0,1,2,..-----------------#
			#1  		|  			|
			#2			|			|
			#3----------0-----------| 	
			#4  		| 0 		|
			#5  		|  			|
			#6----------------------# 
ball = pygame.Rect(screen_width/2-15,screen_height/2-15, 30, 30)
player = pygame.Rect(screen_width-10, screen_height / 2-70 , 10,140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10,140)


#----------------------------------End Drawing phase End----------------------------------



while True:
	#Handling input
	#--pygame.event.get()--get events from the queue. NB it return a list
	for event in pygame.event.get():
		#--pygame.QUIT--checks if the Event object’s type is equal to the constant QUIT
		if event.type == pygame.QUIT:
			#--pygame.quit()--deactivates the Pygame library. Your programs should always 
			# call pygame.quit() before they call sys.exit() to terminate the program.
			pygame.quit()
			sys.exit()
			#----------------------------------Input phase----------------------------------
			#--pygame.KEYDOWN-- checks if any key is pressed 
		if event.type == pygame.KEYDOWN:
			#--pygame.KEYDOWN-- checks a specific key
			#--event.key-- store the key you pressed 
			#--pygame.K_UP:-- is upkey
			if event.key == pygame.K_UP:
				#NB you cant do this player.y+=7 here, because pygame checks if the button changes it state
				#from unpressed to pressed. so if you keep it push down it will not trigger
				# the event. you will need to continously press the button to move in tiny
				#steps which would not be fun. to solve it here is the steps
				# - declaire your varible , speed varivle
				# - add this speed to the player on every single cylele of the loop
				# - if no button is pressed, 
				# - how ever whe the up or the down key is pressed
				#player_speed -= 10 this variable is zero the variable becomes +ive or -ive
				player_speed -= 10
			if event.key == pygame.K_DOWN:
				#player_speed += 10
				player_speed += 10

			#--pygame.KEYUp-- checks if any key is release
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				player_speed += 10
			if event.key == pygame.K_DOWN:
				player_speed -= 10	
			#----------------------------------Input phase----------------------------------
			
	# Game logic
	ball_animation()
	player_animation()
	opponent_ai()
			

	#----------------------------------End Drawing phase End----------------------------------

	# Visuals 
	#--screen.fill(VariavleColor)--add background color
	screen.fill(bg_color)
	#--display surface. the parent surface and we can only have one.
	#---pygame.draw.OBJECT(display surface, color, rect)--- use to display itmes on your parent surface 
	pygame.draw.rect(screen, light_grey, player)
	pygame.draw.rect(screen, light_grey, opponent) 
	pygame.draw.ellipse(screen, light_grey, ball)

	#aaline(surface, color, start_pos, end_pos)
	#aaline(surface, color, (x,y), (x,y))
	pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0),(screen_width / 2, screen_height))
	pygame.draw.aaline(screen, light_grey, (0,screen_height/2),(screen_width , screen_height/2))
	
	

	#----------------------------------End Drawing phase End----------------------------------




	# Updating the window 
	#--pygame.display.flip()--Update the full display Surface to the screen
	pygame.display.flip()

	#FPS, Frames Per Second, is the number of frames shown per unit of time.
	# 1 / FPS is the amount of time should pass between each frame.
	# Tick is just a measure of time in PyGame.
	# clock.tick(40) means that 40 frames should pass (for every second at most) per second
	# NBthe .clock.tick(60) limite how fast our loop runs. important because the computer
	# will try to run the code as fast as it can and hence we may not see the anything
	clock.tick(60)