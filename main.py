from Stages.baseStageClass import BaseStage
from Stages.MainMenu import MainMenu
import pygame
from Map.map import Map

baseScreen = BaseStage(1300, 700)

pygame.init()
mainMenu = MainMenu(baseScreen)
mymap = Map(baseScreen, 1300, 700, "Tyrlian")
if not mainMenu.mainLoop():
    pygame.quit()
elif mainMenu.mainLoop():
    mymap.mainLoop()