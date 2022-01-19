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
#--display.set_mode((screen_width,screen_height))-- return a display surface object
screen = pygame.display.set_mode((screen_width,screen_height))

#--pygame.display.set_caption('Pong')-- given the window or sreen a title
pygame.display.set_caption('Pong')

while True:
	#Handling input
	#--pygame.event.get()--get events from the queue
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	# Updating the window 
	pygame.display.flip()
	clock.tick(60)