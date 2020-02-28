from Stages.baseStageClass import BaseStage
from Stages.MainMenu import MainMenu
import pygame
from Map.map import Map
from Stages.treasureRoom import TreasureRoom
from Stages.encounterStage import EncounterStage
from Stages.Snake.snakeGame import SnakeGame

from Characters.playerClasses.warlock import Warlock
from Characters.playerClasses.fighter import Fighter
from Characters.playerClasses.oldLady import OldLady
from Characters.playerClasses.healer import Healer
#from Stages.loadingScreen import LoadingScreen

baseScreen = BaseStage(1300, 700)



def running(seed):
    pygame.init()
    mainMenu = MainMenu(baseScreen, seed)
    #loadingScreen = LoadingScreen(baseScreen)
    loop = mainMenu.mainLoop()
    # team = [Warlock(), Fighter(), OldLady()]
    team = [Warlock(), Fighter()]
    mymap = Map(baseScreen, loop[1])
    if not loop[0]:
        pygame.quit()
    elif loop[0]:
        current_room_cr = "b"
        count = 0
        cr = 4
        while current_room_cr:
            mymap.screen.bgImage = pygame.transform.scale(pygame.image.load('Map/media/paper.jpg').convert(),
                                                          (mymap.screen.screen_height - 550,
                                                           mymap.screen.screen_width))
            if count >= 3:
                if cr > 12:
                    cr += 1
                count -= 3
            #LoadingScreen.mainLoop()
            current_room_cr = mymap.mainloop()
            if current_room_cr[0] == "b":
                #LoadingScreen.mainLoop()
                EncounterStage(baseScreen,"Stages/media/MainMenueBackground2.png",cr, team)
                pass
            elif current_room_cr[0] == "T":
                #LoadingScreen.mainLoop()
                treasureRoom = TreasureRoom(baseScreen)
                #treasureRoom.mainLoop()
            elif current_room_cr[0] == "P":
                #LoadingScreen.mainLoop()
                snake = SnakeGame(baseScreen, "")
                snake.mainLoop()
                pass
            elif current_room_cr[0] == "B":
                #LoadingScreen.mainLoop()
                encounterStage = EncounterStage(baseScreen,"Stages/media/MainMenueBackground2.png",cr, team)
            elif current_room_cr[0] == "?":
                #LoadingScreen.mainLoop()
                pass
            if current_room_cr == "m":
                running(loop[1])
                pygame.quit()
                exit(0)
            count += 1


if __name__ == "__main__":
    seed = "Best seed"
    running(seed)
