import pygame
from pygame.locals import *

pygame.init()

running = True
size = width,height = (800,800)
road_w = int(width/1.6)

#set window size
screen = pygame.display.set_mode(size)
#set window title
pygame.display.set_caption("Quicky Car Pygame")
#set BG color
screen.fill((60,220,0))

pygame.draw.rect(
	screen,(50,50,50),
	(width/2-road_w/2, 0 , road_w , height))


#apply changes
pygame.display.update()

#keeping window open
while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False


pygame.quit()