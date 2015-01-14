# 1 - Import library
import pygame
from pygame.locals import *
from loadImage import *
from config import *
import warnings
warnings.filterwarnings("ignore")

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
                # print (Index_to_GridXY2(i))
                screen.blit(getPic(level_ele[eachkey][i]), Index_to_GridXY2(i))
    # pygame.display.flip()
    for eachkey in grid_ele:
        ix, iy = int(eachkey[1]), int(eachkey[3])
        gridX, gridY = Index_to_GridXY3(ix + 9 * iy)
        screen.blit(getPic(grid_ele[eachkey]), (gridX, gridY))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            posX, posY=pygame.mouse.get_pos()
            getChooseArea(posX, posY)
            if choose_area == 3:  # 点选的是元素区域
                ele_iX=(posX - bg_ele_rect[0]) // 65
                ele_iY = (posY - bg_ele_rect[1]) // 65
                choose_ele_grid = [ele_iX, ele_iY]
                getChoose_ele(choose_ele_grid)
            if choose_area == 2:  # 点选的是盘面区域
                board_iX = (posX - bg_board_rect[0]) // 65
                board_iY = (posY - bg_board_rect[1]) // 65
                choose_board = [board_iX, board_iY]
                if choose_ele != None:
                    nodelist = find_nodes(
                        tree_lc, './level[%s]/grid[%s]/basic' % (levelId, board_iX + 9 * board_iY))
                    change_node_properties(
                        nodelist, kv_map['%s'], False % (choose_ele))

    pygame.display.update()
