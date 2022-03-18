#sys is a modul to acces some functionality in your system
import pygame, sys

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