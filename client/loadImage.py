import pygame
from pygame.locals import *

#屏幕界面
screen_size = (screen_width, screen_height) = (1570, 649)
screen = pygame.display.set_mode(screen_size)

#底层
bg_board = pygame.image.load("res/scene/bg_board.png")
bg_ele = pygame.image.load("res/scene/bg_ele.png")

bg_board_rect = [130,0,bg_board.get_width(),bg_board.get_height()]
bg_ele_rect = [726,0,bg_ele.get_width(),bg_ele.get_height()]

#元素
def getPic(ele,path='res/element/'):
	'''根据elementID和路径，获取ele对应的图片'''
	return pygame.image.load(path+str(ele)+'.png')



