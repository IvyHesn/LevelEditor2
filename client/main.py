# 1 - Import library
import pygame
from pygame.locals import *
from loadImage import *

pygame.init()
pygame.display.set_caption('LevelEditor!')

while 1:
    screen.fill((255, 255, 255))
    screen.blit(bg_board, bg_board_rect[0:2])
    screen.blit(bg_ele, bg_ele_rect[0:2])
    # screen.blit(getPic(51),(130,0))
    # screen.blit(getPic(0),(130,0))
    for eachkey in level_ele:
        for i in range(0, len(level_ele[eachkey])):
            if level_ele[eachkey][i] != None:
                #print (Index_to_GridXY(i))
                screen.blit(getPic(level_ele[eachkey][i]), Index_to_GridXY(i))
    # pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            posX, posY = pygame.mouse.get_pos()
            PosXY_to_iXY(posX, posY)

    pygame.display.update()
