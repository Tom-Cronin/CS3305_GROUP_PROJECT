from Stages.baseStageClass import BaseStage
from Stages.MainMenu import MainMenu
import pygame
from Map.map import Map
from Stages.treasureRoom import TreasureRoom
from Stages.encounterStage import EncounterStage

from Characters.playerClasses.warlock import Warlock
#from Stages.loadingScreen import LoadingScreen

baseScreen = BaseStage(1300, 700)


def running():
    pygame.init()
    mainMenu = MainMenu(baseScreen)
    #map takes the screen and the map seed as input
    mymap = Map(baseScreen, "Best seed")
    #loading screen takes the screen as input
    #loadingScreen = LoadingScreen(baseScreen)
    loop = mainMenu.mainLoop()
    if not loop:
        pygame.quit()
    elif loop:
        mymap.screen.bgImage = pygame.transform.scale(pygame.image.load('Map/media/paper.jpg').convert(),
                                                      (mymap.screen.screen_height - 550,
                                                       mymap.screen.screen_width))
        current_room_cr = "b"
        count = 0
        cr = 4
        while current_room_cr:
            if count >= 3:
                cr += 1
                count -= 3
            #LoadingScreen.mainLoop()
            current_room_cr = mymap.mainloop()
            if current_room_cr[0] == "b":
                #LoadingScreen.mainLoop()
                #encounter takes the screen and the current challange rating as input
                EncounterStage(baseScreen,"Stages/media/MainMenueBackground2.png",cr, [Warlock()])
                #encounterStage.mainLoop()
                pass
            elif current_room_cr[0] == "T":
                #LoadingScreen.mainLoop()
                #the treasure room takes the screen as input
                treasureRoom = TreasureRoom(baseScreen)
                treasureRoom.mainloop()
            elif current_room_cr[0] == "P":
                #LoadingScreen.mainLoop()
                #the puzzle room takes the screen as input
                print("It's a puzzle room and the current cr is " + str(cr))
            elif current_room_cr[0] == "B":
                #LoadingScreen.mainLoop()
                #the boss encounter stage takes the base screen and the current
                #challange rating as input
                encounterStage = EncounterStage(baseScreen,"Stages/media/MainMenueBackground2.png",cr, [Warlock()])
                # encounterStage.mainLoop()
            elif current_room_cr[0] == "?":
                #LoadingScreen.mainLoop()
                #the mystery room takes the screen as input
                print("It's a ? room and the current cr is " + str(cr))
            if current_room_cr == "m":
                running()
                pygame.quit()
            count += 1


if __name__ == "__main__":
    running()
