from Stages.baseStageClass import BaseStage
from Stages.MainMenu import MainMenu
import pygame
from Map.map import Map

baseScreen = BaseStage(1300, 700)


def running():
    pygame.init()
    mainMenu = MainMenu(baseScreen)
    mymap = Map(baseScreen, "Best seed")
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
            print("Loading screen")
            print("map")
            current_room_cr = mymap.mainloop()
            if current_room_cr == "b":
                print("Loading screen")
                print("It's a battle room and the current cr is " + str(cr))
            elif current_room_cr == "T":
                print("Loading screen")
                print("It's a treasure room and the current cr is " + str(cr))
            elif current_room_cr == "P":
                print("Loading screen")
                print("It's a puzzle room and the current cr is " + str(cr))
            elif current_room_cr == "B":
                print("Loading screen")
                print("It's a Boss room and the current cr is " + str(cr))
            elif current_room_cr == "?":
                print("Loading screen")
                print("It's a ? room and the current cr is " + str(cr))
            if current_room_cr == "m":
                running()
                pygame.quit()
            count += 1


if __name__ == "__main__":
    running()
