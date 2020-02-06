from Stages.baseStageClass import BaseStage
from Stages.MainMenu import MainMenu
import pygame
from Map.map import Map

baseScreen = BaseStage(1300, 700)

pygame.init()
mainMenu = MainMenu(baseScreen)
mymap = Map(baseScreen, "Best seed")
if mainMenu.mainLoop() == False:
    pygame.quit()
elif mainMenu.mainLoop() == True:
    current_room_cr = ["b", 4, 0]
    while current_room_cr[2] != 1:
        print("Loading screen")
        print("map")
        current_room_cr = mymap.mainLoop()
        if current_room_cr[0] == "b":
            print("Loading screen")
            print("It's a battle room and the current cr is " + str(current_room_cr[1]))
        elif current_room_cr[0] == "T":
            print("Loading screen")
            print("It's a treasure room and the current cr is " + str(current_room_cr[1]))
        elif current_room_cr[0] == "P":
            print("Loading screen")
            print("It's a puzzle room and the current cr is " + str(current_room_cr[1]))
        elif current_room_cr[0] == "B":
            print("Loading screen")
            print("It's a Boss room and the current cr is " + str(current_room_cr[1]))
        elif current_room_cr[0] == "?":
            print("Loading screen")
            print("It's a ? room and the current cr is " + str(current_room_cr[1]))