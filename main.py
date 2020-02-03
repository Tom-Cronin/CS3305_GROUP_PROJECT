from Stages.baseStageClass import BaseStage
from Stages.MainMenu import MainMenu
import pygame
from pygame.locals import *

pygame.init()
mainMenu = MainMenu(1300, 700)
if mainMenu.mainLoop() == False:
    pygame.quit()
elif mainMenu.mainLoop() == True:
    print("Game Start")
    pygame.quit()