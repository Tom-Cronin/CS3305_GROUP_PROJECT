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
        self.square2 = SnakeSquares(self.positionX+10, self.positionY, 2)
        self.square3 = SnakeSquares(self.positionX+20, self.positionY, 3)
        self.squares = [self.square1, self.square2, self.square3]
        self.head = self.square3
        self.mazeColor = (34, 139, 34)
        self.direction = "R"   # for image rotation
        self.prevDirection = "R"

    def draw(self, turn180=False):
        #ToDO: Use self.direction and a loop to determine the rotation of each square, print head, a loop for body, tail
        head = pygame.transform.scale((pygame.image.load("Stages/media/snakeHead.png").convert_alpha()), (10, 10))
        body = pygame.transform.scale((pygame.image.load("Stages/media/SnakeBody.png").convert_alpha()), (10, 10))
        tail = pygame.transform.scale((pygame.image.load("Stages/media/SnakeTail.png").convert_alpha()), (10, 10))

        x = 0
        if self.head.direction == "R":
            x = 270
        elif self.head.direction == "L":
            x = 90
        elif self.head.direction == "D":
            x = 180

        head = pygame.transform.rotate(head, x)

        x = 0
        if self.prevDirection == "R":
            x = 270
        elif self.prevDirection == "L":
            x = 90
        elif self.prevDirection == "D":
            x = 180

        tail = pygame.transform.rotate(tail, x)

        for i in range(1, len(self.squares)-1):
            self.erase(self.squares[i].Rect)
            body = pygame.transform.rotate(body, x)
            self.display.blit(body, (self.squares[i].x, self.squares[i].y))

        self.erase(self.square1.Rect)
        self.erase(self.square3.Rect)
        if self.head.num == self.square3.num:
            self.display.blit(head, (self.square3.x, self.square3.y))
            if turn180 is False:
                self.display.blit(tail, (self.square1.x, self.square1.y))
        else:
            self.display.blit(head, (self.square1.x, self.square1.y))
            if turn180 is False:
                self.display.blit(tail, (self.square3.x, self.square3.y))

    def erase(self, squareRect):
            pygame.draw.rect(self.display, self.mazeColor, squareRect)

    def check180(self, direction):
        if (self.direction == "U" and direction == "D") or (
                self.direction == "D" and direction == "U") or (
                self.direction == "L" and direction == "R") or (
                self.direction == "R" and direction == "L"):
            return True
        return False

    def move(self, direction):
        turn180 = False
        if self.check180(direction) is True:
            # If making a 180 degree turn, the tail will NOT be put on top of the head
            turn180 = True
        squares = self.squares
        if self.head.num == 3:
            oldRect = self.square1.Rect  # square to be erased
            squares[0] = self.square1
            squares[len(squares)-1] = self.square3 # sets order of movement for squares

        else:
            oldRect = self.square3.Rect
            squares[0] = self.square3
            squares[len(squares)-1] = self.square1

        # each square (other than the head square) follows the square in front of it

        i = 1
        while i < len(squares):
            squares[i-1].xUpdate(squares[i].x)
            squares[i - 1].yUpdate(squares[i].y)
            squares[i - 1].direction = squares[i].direction
            i += 1

        self.erase(oldRect)

        # Moves the head square in the correct direction
        self.prevDirection = self.direction
        self.head.direction = direction
        if direction == "R":
            self.head.x += 10
            self.head.xUpdate(self.head.x)
        elif direction == "L":
            self.head.x -= 10
            self.head.xUpdate(self.head.x)
        elif direction == "U":
            self.head.y -= 10
            self.head.yUpdate(self.head.y)
        elif direction == "D":
            self.head.y += 10
            self.head.yUpdate(self.head.y)

        self.head = self.square1  # Updates the head of the snake

        self.direction = direction
        # Update positions of squares in maze
        self.draw(turn180)
        pygame.display.update(self.mazeRect)



class SnakeSquares:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.size = 10
        self.Rect = None
        self.buildRect()
        self.num = num
        self.direction = "R"

    def buildRect(self):
        self.Rect = Rect((self.x, self.y, self.size, self.size))

    def xUpdate(self, x):
        self.x = x
        self.buildRect()

    def yUpdate(self, y):
        self.y = y
        self.buildRect()
