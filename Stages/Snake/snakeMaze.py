import pygame
from pygame.locals import *

class Maze:
    def __init__(self, screen_height, screen_width, display, num = 1):
        self.y = 100
        self.height = screen_height-320
        self.x = 100
        self.width = screen_width
        self.mazeColor = (34, 139, 34)  # forest green
        self.wallColor = (0, 0, 0)  # black
        self.mazeRect = Rect(self.x, self.y, self.width, self.height)
        self.display = display
        self.mazeNum = num  # Potential to make multiple mazes
        self.walls = []
        self.exit = None
        self.generateMaze()

    def draw(self):
        self.drawBackground()
        self.drawWalls()

    def drawBackground(self):
        pygame.draw.rect(self.display, self.mazeColor, self.mazeRect)

    def drawWalls(self):
        for wall in self.walls:
            pygame.draw.rect(self.display, self.wallColor, wall.Rect)
        # draw entry and exit spots
        pygame.draw.rect(self.display, self.mazeColor, self.exit.Rect)

    def constructWallH(self, x, y, len):
        # (x location on drawing, y location on drawing, x1 - x2 on drawing)
        self.walls.append(Walls(self.x+(x*10), self.y+(y*10), (len+1)*10, "h"))
        
    def constructWallV(self, x, y, len): # takes in values as number of squares
        self.walls.append(Walls(self.x+(x*10), self.y+(y*10), (len+1)*10))

    def generateMaze(self):
        # BorderWalls
        self.walls.append(Walls(self.x, self.y, self.width, "h"))  # Top border
        self.walls.append(Walls(self.x, self.y, self.height))  # Left border
        self.walls.append(Walls(self.x+self.width-10, self.y, self.height))  # right border
        self.walls.append(Walls(self.x, self.y+self.height-10, self.width, "h"))  # bottom border
        if self.mazeNum == 1:
            # Destination:
            self.exit = Walls(self.x + self.width - 10, self.y + 10, 30)  # Destination
            # Horizontal maze walls:
            self.constructWallH(0, 4, 3)
            self.constructWallH(4, 25, 14)
            self.constructWallH(4, 29, 9)
            self.constructWallH(8, 1, 12)

            self.constructWallH(8, 5, 5)
            self.constructWallH(8, 9, 13)
            self.constructWallH(8, 13, 4)
            self.constructWallH(8, 21, 4)

            self.constructWallH(8, 33, 10)
            self.constructWallH(8, 37, 6)
            self.constructWallH(8, 41, 9)
            self.constructWallH(12, 17, 4)
            self.constructWallH(16, 13, 12)
            self.constructWallH(16, 21, 6)
            self.constructWallH(17, 5, 8)
            self.constructWallH(17, 29, 5)

            self.constructWallH(18, 43, 8)
            self.constructWallH(20, 17, 15)
            self.constructWallH(22, 33, 4)
            self.constructWallH(22, 37, 8)

            self.constructWallH(25, 4, 4)
            self.constructWallH(25, 9, 15)
            self.constructWallH(30, 21, 6)
            self.constructWallH(30, 43, 4)

            self.constructWallH(33, 5, 3)
            self.constructWallH(34, 26, 6)
            self.constructWallH(36, 13, 8)
            self.constructWallH(38, 30, 20)

            self.constructWallH(40, 17, 15)
            self.constructWallH(42, 34, 13)
            self.constructWallH(46, 38, 5)
            self.constructWallH(49, 26, 6)

            self.constructWallH(48, 3, 6)
            self.constructWallH(58, 6, 0)
            self.constructWallH(48, 9, 7)
            self.constructWallH(52, 13, 3)

            self.constructWallH(54, 18, 4)
            self.constructWallH(53, 22, 5)
            self.constructWallH(55, 43, 3)
            # Vertical maze walls:

            self.constructWallV(4, 4, 11)
            self.constructWallV(4, 19, 6)
            self.constructWallV(4, 29, 14)
            self.constructWallV(8, 1, 20)

            self.constructWallV(8, 33, 4)
            self.constructWallV(8, 41, 2)
            self.constructWallV(13, 41, 5)
            self.constructWallV(16, 13, 5)

            self.constructWallV(17, 29, 4)
            self.constructWallV(18, 33, 10)
            self.constructWallV(22, 21, 8)
            self.constructWallV(22, 37, 2)

            self.constructWallV(25, 4, 5)
            self.constructWallV(26, 17, 16)
            self.constructWallV(26, 41, 2)
            self.constructWallV(30, 21, 16)

            self.constructWallV(30, 41, 2)
            self.constructWallV(32, 13, 4)
            self.constructWallV(33, 1, 4)
            self.constructWallV(34, 26, 17)

            self.constructWallV(36, 13, 8)
            self.constructWallV(38, 30, 13)
            self.constructWallV(40, 1, 8)
            self.constructWallV(40, 17, 9)

            self.constructWallV(42, 34, 9)
            self.constructWallV(44, 1, 12)
            self.constructWallV(45, 21, 9)
            self.constructWallV(46, 38, 8)

            self.constructWallV(48, 3, 10)
            self.constructWallV(54, 1, 4)
            self.constructWallV(55, 13, 5)
            self.constructWallV(49, 17, 9)

            self.constructWallV(51, 38, 5)
            self.constructWallV(55, 34, 9)

class Walls:
    def __init__(self, x, y,  length, orientation="v"):
        self.x = x
        self.y = y
        if orientation == "v":
            self.width = 10
            self.height = length
        else:
            self.width = length
            self.height = 10
        self.Rect = None
        self.Rect = Rect((self.x, self.y, self.width, self.height))
