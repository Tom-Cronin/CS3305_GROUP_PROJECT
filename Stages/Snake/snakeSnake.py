import pygame
from pygame.locals import *

class SnakeGuy:
    def __init__(self, display, color, maze):
        self.mazeRect = maze.mazeRect
        self.display = display
        self.color = color
        self.squareSize = 10
        self.positionX = maze.x + 10
        self.positionY = maze.y + 10
        self.square1 = SnakeSquares(self.positionX, self.positionY, 1)
        self.square2 = SnakeSquares(self.positionX+10, self.positionY, 2)
        self.square3 = SnakeSquares(self.positionX+20, self.positionY, 3)
        self.squares = [self.square1, self.square2, self.square3]
        self.head = self.square3
        self.mazeColor = (34, 139, 34)
        self.direction = "R"   # for image rotation
        self.penultimateSquare = self.square2
        self.tail = self.square1

    def draw(self, turn180=False):
        head = pygame.transform.scale((pygame.image.load("Stages/media/snakeHead.png").convert_alpha()), (10, 10))
        bodyImage = pygame.transform.scale((pygame.image.load("Stages/media/SnakeBody.png").convert_alpha()), (10, 10))
        tail = pygame.transform.scale((pygame.image.load("Stages/media/SnakeTail.png").convert_alpha()), (10, 10))

        for square in self.squares:
            x = 0
            if square.direction == "R":
                x = 270
            elif square.direction == "L":
                x = 90
            elif square.direction == "D":
                x = 180

            self.erase(square.Rect)

            if square.num == self.head.num:
                head = pygame.transform.rotate(head, x)
                self.display.blit(head, (square.x, square.y))

            elif square.num == self.tail.num:
                tail = pygame.transform.rotate(tail, x)
                if turn180 is False:
                    self.display.blit(tail, (square.x, square.y))

            else:
                body = bodyImage
                body = pygame.transform.rotate(body, x)
                self.display.blit(body, (square.x, square.y))

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
        oldRect = self.tail.Rect  # square to be erased
        squares[0] = self.tail
        squares[len(squares)-1] = self.head  # sets order of movement for squares

        # each square (other than the head square) follows the square in front of it

        i = 1
        while i < len(squares):
            squares[i-1].xUpdate(squares[i].x)
            squares[i - 1].yUpdate(squares[i].y)
            squares[i - 1].direction = squares[i].direction
            i += 1

        squares[len(squares)-2].direction = direction

        self.erase(oldRect)

        # Moves the head square in the correct direction
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
        self.tail = self.square3

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
