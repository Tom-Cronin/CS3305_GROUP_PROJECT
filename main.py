from Stages.baseStageClass import BaseStage
from Stages.MainMenu import MainMenu
import pygame
from Map.map import Map
from Stages.treasureRoom import TreasureRoom
from Stages.encounterStage import EncounterStage
from Stages.loadingScreen import LoadingScreen

baseScreen = BaseStage(1300, 700)
def running():
    pygame.init()
    mainMenu = MainMenu(baseScreen)
    mymap = Map(baseScreen, "Best seed")
    loadingScreen = LoadingScreen(baseScreen)
    loop = mainMenu.mainLoop()
    if not loop:
        pygame.quit()
    elif loop:
        mymap.screen.bgImage = pygame.transform.scale(pygame.image.load('Map/media/paper.jpg').convert(),
                                                      (mymap.screen.screen_height,
                                                       mymap.screen.screen_width))
        current_room_cr = ["b", 4, 0]
        count = 0
        cr = 4
        while current_room_cr[1] != 1:
            if count >= 3:
                cr += 1
                count -= 3
            LoadingScreen.mainLoop()
            current_room_cr = mymap.mainLoop()
            if current_room_cr[0] == "b":
                LoadingScreen.mainLoop()
                encounterStage = EncounterStage(baseScreen, cr)
                encounterStage.mainLoop()
            elif current_room_cr[0] == "T":
                LoadingScreen.mainLoop()
                treasureRoom = TreasureRoom(baseScreen)
                treasureRoom.mainloop()
            elif current_room_cr[0] == "P":
                LoadingScreen.mainLoop()
                print("It's a puzzle room and the current cr is " + str(cr))
            elif current_room_cr[0] == "B":
                LoadingScreen.mainLoop()
                encounterStage = EncounterStage(baseScreen, cr)
                encounterStage.mainLoop()
            elif current_room_cr[0] == "?":
                LoadingScreen.mainLoop()
                print("It's a ? room and the current cr is " + str(cr))
            if current_room_cr[0] == "m":
                running()
                pygame.quit()
            count += 1

if __name__ == "__main__":
    running()