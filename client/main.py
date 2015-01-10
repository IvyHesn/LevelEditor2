# 1 - Import library
import pygame
from pygame.locals import *
from loadImage import *

pygame.init()
pygame.display.set_caption('LevelEditor!') 

while 1:
	screen.fill((255,255,255))
	screen.blit(bg_board,bg_board_rect[0:2])
	screen.blit(bg_ele,bg_ele_rect[0:2])

	#pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
		if event.type == pygame.MOUSEBUTTONDOWN:
			posX,posY = pygame.mouse.get_pos()

	pygame.display.update()
