from Stages.baseStageClass import BaseStage, StageButton
from Stages.Snake.snakeMaze import Maze
from Stages.Snake.snakeSnake import SnakeGuy, SnakeSquares
from Stages.Snake.snakeGame import SnakeGame
import pygame
import time
from pygame.locals import *
import random

class SnakeFood():
    def __init__(self, maze):
        self.maze = maze
        self.x = None
        self.y = None
        self.size = 10
        self.Rect = None
        self.setXY()

    def setXY(self):
        self.y = random.randint(self.maze.x+10, self.maze.height+80)
        self.x = random.randint(self.maze.y+10, self.maze.width +80)
        self.Rect = Rect((self.x, self.y, self.size, self.size))

class ScoreBox():
    def __init__(self, maze):
        self.score = 0
        self.x = maze.y + maze.width - 20
        self.y = maze.x+20
        self.size = 20
        self.scoreBox = Rect((self.x, self.y, self.size, self.size))
        self.font = 'Stages/media/Chapaza.ttf'
        self.color = (255, 255, 255)  # white
        self.display = maze.display

    def printScore(self):
        font = pygame.font.Font(self.font, 20)
        text = font.render(str(self.score), True, self.color)
        textRect = self.scoreBox
        textRect.center = (self.x, self.y)
        self.display.blit(text, textRect)
        pygame.display.update(textRect)

    def updateScore(self):
        self.score += 1
        self.printScore()

class SnakeGuy2(SnakeGuy):
    def __init__(self, display, color, mazeRect):
        super().__init__(display, color, mazeRect)
        self.bodyLength = 3  # number of body squares

    def eat(self):
        self.bodyLength += 1
        tail = self.squares[len(self.squares)-1]
        self.squares[len(self.squares) - 1] = SnakeSquares(tail.x, tail.y, self.bodyLength)
        self.squares[len(self.squares) - 1].direction = self.penultimateSquare.direction
        self.penultimateSquare = self.squares[len(self.squares) - 1]
        self.squares.append(tail)


class Maze2(Maze):
    def __init__(self, screen_height, screen_width, display):
        super().__init__(screen_height, screen_width, display, 2)
        self.y = 230
        self.height = screen_height - 580
        self.x = 230
        self.width = screen_width - 260
        self.mazeRect = Rect(self.x, self.y, self.width, self.height)
        self.walls = []
        self.generateMaze()

class SnakeGame2(SnakeGame):

    def __init__(self, screen_height, screen_width):
        gameHint = "Eat 10 squares\nUse the arrow keys to move\nIf you eat yourself, you will die\n" \
                   "If you hit a wall you will die"
        super().__init__(screen_height, screen_width, gameHint)
        self.maze = Maze2(screen_height, screen_width, self.display)
        self.snake = SnakeGuy2(self.display, self.snakeColor, self.maze)
        self.food = SnakeFood(self.maze)

        self.food_color = (0, 0, 0)  # black
        self.score = ScoreBox(self.maze)
        self.snake.move("R")
        self.snake.move("R")
        self.snake.move("R")  # This technically solves the moving/snake image break at the start of the game

    def listenSnake(self):
        # Checks if snake should move:
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            if self.snake.check180("U") is False:
                self.snake.move("U")
                self.checkLocation()
        elif key[pygame.K_DOWN]:
            if self.snake.check180("D") is False:
                self.snake.move("D")
                self.checkLocation()
        elif key[pygame.K_RIGHT]:
            if self.snake.check180("R") is False:
                self.snake.move("R")
                self.checkLocation()
        elif key[pygame.K_LEFT]:
            if self.snake.check180("L") is False:
                self.snake.move("L")
                self.checkLocation()

        time.sleep(0.1)

    def dropFood(self):
        oldRect = self.food.Rect
        self.food.setXY()
        self.eraseRect(oldRect)
        pygame.display.update(oldRect)
        pygame.draw.rect(self.display, self.food_color, self.food.Rect)
        pygame.display.update(self.food.Rect)
        self.snakeLayer()
        # ToDo: prevent food from appearing in scorebox

    def foodLayer(self):
        pygame.draw.rect(self.display, self.food_color, self.food.Rect)

    def eraseRect(self, squareRect):
            pygame.draw.rect(self.display, self.maze.mazeColor, squareRect)

    def checkLocation(self):
        # Checks if snake has crashed into wall or reached its destination:
        # if head crashes into another square: die
        if self.food.x-9 <= self.snake.head.x <= (self.food.x+9):
            if self.food.y-9 <= self.snake.head.y <= (self.food.y+9):
                self.eraseRect(self.score.scoreBox)
                self.score.updateScore()
                self.snake.eat()
                if self.score.score == 10:
                    self.gameOver(True)
                else:
                    self.dropFood()
        else:
            x = len(self.snake.squares) - 1
            for square in self.snake.squares[:x]:
                if self.snake.head.x == square.x and self.snake.head.y == square.y:
                    return self.gameOver()
            for wall in self.maze.walls:
                if wall.x <= self.snake.head.x <= (wall.x + wall.width-1):
                    if wall.y <= self.snake.head.y <= (wall.y + wall.height-1):
                        return self.gameOver()

    def mainLoop(self):  # listens for events
        self.backgroundLayer()
        self.mazeLayer()
        self.foodLayer()
        self.snakeLayer()
        self.score.printScore()

        pygame.display.update()

        mainLoop = True

        while mainLoop:
            self.listenMouse()
            self.listenButton()
            if self.finished is False and self.disabled is False:
                self.listenSnake()
                self.snake.move(self.snake.direction)  # keeps snake moving
                self.checkLocation()
                time.sleep(0.2)  # Can reduce time to increase difficulty level
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainLoop = False

pygame.init()
puzzle = SnakeGame2(800, 600)
puzzle.mainLoop()
pygame.quit()