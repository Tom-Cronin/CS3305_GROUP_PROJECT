from Stages.baseStageClass import BaseStage
from gridButton import GridButton
import pygame
from pygame.locals import *
import time


class SlidingPuzzle(BaseStage):
    def __init__(self, screen_height, screen_width):

        super().__init__(screen_height, screen_width)
        self.activeButtons = [self.quitGame]
        self.finished = False

    def mainloop(self):
        self.backgroundLayer()
        pygame.display.update()

        loop = True

        b = GridButton(self.display, 1, 'Map/media/paper.jpg', 0, 0)
        b.draw()

        while loop:
            self.listenMouse()
            if self.finished is False:
                self.listenMouse()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False


pygame.init()
puzzle = SlidingPuzzle(800, 600)
puzzle.mainloop()
pygame.quit()