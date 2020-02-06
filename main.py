from Stages.baseStageClass import BaseStage
from Stages.MainMenu import MainMenu
import pygame
from Map.map import Map

baseScreen = BaseStage(1300, 700)

pygame.init()
mainMenu = MainMenu(baseScreen)
mymap = Map(baseScreen, "Tyrlian")
if mainMenu.mainLoop() == False:
    pygame.quit()
elif mainMenu.mainLoop() == True:
    mymap.mainLoop()