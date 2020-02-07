import pygame
from pygame.locals import *

class SnakeGuy:
    def __init__(self, display, color, mazeRect):
        self.mazeRect = mazeRect
        self.display = display
        self.color = color
        self.squareSize = 10
        self.positionX = 120
        self.positionY = 120
        self.square1 = SnakeSquares(self.positionX, self.positionY, 1)
        self.square2 = SnakeSquares(self.positionX+10, self.positionY, 2 )
        self.square3 = SnakeSquares(self.positionX+20, self.positionY, 3)
        self.squares = [self.square1, self.square2, self.square3]
        self.head = self.square3
        self.mazeColor = (34, 139, 34)
        self.currentPos = 1

    def draw(self):
        x = 255
        for square in self.squares:
            pygame.draw.rect(self.display, (x, 0, 0), square.Rect)
            x -= 70

    def erase(self, squareRect):
            pygame.draw.rect(self.display, self.mazeColor, squareRect)

    def move(self, direction):
        if self.head.num == 3:
            oldRect = self.square1.Rect # square to be erased
            squares = [self.square1, self.square2, self.head]  # sets order of movement for squares
        else:
            oldRect = self.square3.Rect
            squares = [self.square3, self.square2, self.head]

        # each square (other than the head square) follows the square in front of it
        i = 1
        while i < len(squares):
            squares[i-1].xUpdate(squares[i].x)
            squares[i - 1].yUpdate(squares[i].y)
            i += 1

        self.erase(oldRect)

        # Moves the head square in the correct direction
        if direction == "Right":
            self.head.x += 10
            self.head.xUpdate(self.head.x)
        elif direction == "Left":
            self.head.x -= 10
            self.head.xUpdate(self.head.x)
        elif direction == "Up":
            self.head.y -= 10
            self.head.yUpdate(self.head.y)
        elif direction == "Down":
            self.head.y += 10
            self.head.yUpdate(self.head.y)

        # Update positions of squares in maze
        self.draw()
        pygame.display.update(self.mazeRect)

        self.head = self.square1 # Updates the head of the snake

class SnakeSquares:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.size = 10
        self.Rect = None
        self.buildRect()
        self.num = num

    def buildRect(self):
        self.Rect = Rect((self.x, self.y, self.size, self.size))

    def xUpdate(self, x):
        self.x = x
        self.buildRect()

    def yUpdate(self, y):
        self.y = y
        self.buildRect()
