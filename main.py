from Stages.baseStageClass import BaseStage
from Stages.MainMenu import MainMenu
import pygame
from Map.map import Map

from Stages.treasureRoom import TreasureRoom
from Stages.encounterStage import EncounterStage
from Stages.healingRoom import HealStage
from Stages.Snake.snakeGame import SnakeGame
from Stages.Snake1.SnakeGame1 import SnakeGame1
from Stages.Snake2.snakeGame2 import SnakeGame2
from Stages.Match.matchGame import MatchGame

import random
import string

from Characters.playerClasses.warlock import Warlock
from Characters.playerClasses.fighter import Fighter
from Characters.playerClasses.oldLady import OldLady
from Characters.playerClasses.healer import Healer
from Stages.LoadingScreen import LoadingScreen

baseScreen = BaseStage(1300, 700)

def running(seed):
    pygame.init()
    pygame.display.set_caption('Traylian')
    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
    mainMenu = MainMenu(baseScreen, seed)
    team = [Warlock(), Fighter(), OldLady(), Healer()]
    load = LoadingScreen(baseScreen, team)
    loop = mainMenu.mainLoop()
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
                if cr < 12:
                    cr += 1
                count -= 3

            load.cleanUp()
            current_room_cr = mymap.mainloop()
            if current_room_cr[0] == "b":
                load.mainloop()
                EncounterStage(baseScreen,"Stages/media/MainMenueBackground2.png",cr, team)

            elif current_room_cr[0] == "T":
                load.mainloop()
                treasureRoom = TreasureRoom(baseScreen, team)
                treasureRoom.mainLoop()

            elif current_room_cr[0] == "H":
                myHealStage = HealStage(baseScreen,team)
                myHealStage.mainLoop()

            elif current_room_cr[0] == "P":
                load.mainloop()
                puzzle = random.choice([0,1,2])
                if puzzle == 0:
                    snake = SnakeGame1(baseScreen, team)
                    snake.mainLoop()
                elif puzzle == 1:
                    snake1 = SnakeGame2(baseScreen, team)
                    snake1.mainLoop()
                elif puzzle == 2:
                    match = MatchGame(baseScreen, team, cr)
                    match.mainLoop()
            elif current_room_cr[0] == "B":
                load.mainloop()
                EncounterStage(baseScreen,"assets/images/characters/Players/PNG_Images/IronBoss/BG_Castle.png",cr, team, True)
                for char in team:
                    char.charFullLevelUp()
            elif current_room_cr[0] == "?":
                room = random.choice(["b", "p", "H"])
                if room == "H":
                    myHealStage = HealStage(baseScreen, team)
                    myHealStage.mainLoop()
                elif room == "p":
                    puzzle = random.choice([0, 1, 2])
                    if puzzle == 0:
                        snake = SnakeGame1(baseScreen, team)
                        snake.mainLoop()
                    elif puzzle == 1:
                        snake1 = SnakeGame2(baseScreen, team)
                        snake1.mainLoop()
                    elif puzzle == 2:
                        match = MatchGame(baseScreen, team, cr)
                        match.mainLoop()
                else:
                    EncounterStage(baseScreen, "Stages/media/MainMenueBackground2.png", cr, team)

                load.mainloop()
                pass
            if current_room_cr == "m":
                running(loop[1])
                pygame.quit()
                exit(0)
            if len(team) <= 0:
                running(seed)
            count += 1


if __name__ == "__main__":
    seed = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(16)])
    running(seed)
