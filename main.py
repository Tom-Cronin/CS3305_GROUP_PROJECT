from Stages.baseStageClass import BaseStage
from Stages.MainMenu import MainMenu
import pygame
from Map.map import Map
from Stages.treasureRoom import TreasureRoom
from Stages.encounterStage import EncounterStage
from Stages.Snake.snakeGame import SnakeGame

import random
import string

from Characters.playerClasses.warlock import Warlock
from Characters.playerClasses.fighter import Fighter
from Characters.playerClasses.oldLady import OldLady
from Characters.playerClasses.healer import Healer
#from Stages.loadingScreen import LoadingScreen

baseScreen = BaseStage(1300, 700)



def running(seed):
    seed = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(16)])
    pygame.init()
    pygame.display.set_caption('Traylian')
    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
    mainMenu = MainMenu(baseScreen, seed)
    #loadingScreen = LoadingScreen(baseScreen)
    loop = mainMenu.mainLoop()
    team = [Warlock(), Fighter(), OldLady(),Healer()]
    # team = [Warlock(), Fighter()]
    # demoBattle = False
    # demoTreasure = False
    # demoPuzzle = False
    # demoMystery = False
    # demoBoss = True
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
                demoBattle = False
                #LoadingScreen.mainLoop()
                EncounterStage(baseScreen,"Stages/media/MainMenueBackground2.png",cr, team)
                pass
            elif current_room_cr[0] == "T":
                demoTreasure = False
                #LoadingScreen.mainLoop()
                treasureRoom = TreasureRoom(baseScreen)
                #treasureRoom.mainLoop()

            elif current_room_cr[0] == "H":
                # ToDo implement room for healing
                # Only quick logic
                for ally in team:
                    ally.health = ally.maxHealth

            elif current_room_cr[0] == "P":
                demoPuzzle = False
                #LoadingScreen.mainLoop()
                snake = SnakeGame(baseScreen, "", team)
                snake.mainLoop()
                pass
            elif current_room_cr[0] == "B":
                demoBoss = False
                #LoadingScreen.mainLoop()
                EncounterStage(baseScreen,"assets/images/characters/Players/PNG_Images/IronBoss/BG_Castle.png",cr, team, True)
            elif current_room_cr[0] == "?":

                demoMystery = False
                #LoadingScreen.mainLoop()
                pass
            if current_room_cr == "m":
                running(loop[1])
                pygame.quit()
                exit(0)
            count += 1


if __name__ == "__main__":
    seed = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(16)])
    # seed = "Best seed"
    running(seed)
