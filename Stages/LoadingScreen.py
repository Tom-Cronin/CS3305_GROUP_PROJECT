import pygame, sys
from pygame.locals import *
from Stages.baseStageClass import *
import time

class LoadingScreen:
    def __init__(self, screen):
        self.baseScreen = screen

    def backgroundLayer(self):
        self.baseScreen.display.blit(self.baseScreen.bgImage, (0, 0))
        pygame.draw.rect(self.baseScreen.display, (120, 120, 120), (0, 550, self.baseScreen.screen_height, 50))
        pygame.display.update()

    def mainloop(self):
        self.backgroundLayer()
        time.sleep(10)