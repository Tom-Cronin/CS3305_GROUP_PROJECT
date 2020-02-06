import pygame
from pygame.locals import *

class Maze:
    def __init__(self, screen_height, screen_width, display):
        self.y = 100
        self.height = screen_height-300
        self.x = 100
        self.width = screen_width
        self.mazeColor = (34, 139, 34)  # forest green
        self.mazeRect = Rect(self.x, self.y, self.width, self.height)
        self.display = display

    def draw(self):
        self.drawBackground()
        self.drawWalls()

    def drawBackground(self):
        pygame.draw.rect(self.display, self.mazeColor, self.mazeRect)

    def drawWalls(self):
        pass

class Walls:
    pass