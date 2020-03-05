import pygame
from pygame.locals import *


class GridButton:
    def __init__(self, display, position, image, x, y):
        self.display = display
        self.position = position
        self.backgroundColour = (0, 0, 0)
        self.image = image
        self.backgroundX = x
        self.backgroundY = y
        self.imageX = x + 2
        self.imageY = y + 2
        self.sideLength = 50

    def draw(self):
        #pygame.draw.rect(self.display, self.backgroundColour, (self.backgroundX, self.backgroundY, self.sideLength))
        #self.display.blit(self.image, (self.imageX, self.imageY))
        self.display.blit(self.bgImage, (0, 0))