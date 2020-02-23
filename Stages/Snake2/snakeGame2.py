from Stages.baseStageClass import BaseStage, StageButton
from Stages.Snake.snakeMaze import Maze
from Stages.Snake.snakeSnake import SnakeGuy
from Stages.Snake.snakeGame import SnakeGame
import pygame
import time
from pygame.locals import *
import random

class SnakeFood():
    def __init__(self, maze_width, maze_height):
        self.maze_width = maze_width
        self.maze_height = maze_height
        self.x = None
        self.y = None
        self.size = 10
        self.Rect = None
        self.setXY()

    def setXY(self):
        self.y = random.randint(110, self.maze_height+80)
        self.x = random.randint(110, self.maze_width +80)
        self.Rect = Rect((self.x, self.y, self.size, self.size))

class ScoreBox():
    def __init__(self, maze):
        self.score = 0
        self.x = maze.y + maze.width - 20
        self.y = maze.x+20
        self.size = 20
        self.scoreBox = Rect((self.x, self.y, self.size, self.size))
        print(self.scoreBox)
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
        self.bodyLength = 1  # number of middle body squares, excludes head and tail

class SnakeGame2(SnakeGame):

    def __init__(self, screen_height, screen_width):
        gameHint = "Eat 10 squares\nUse the arrow keys to move\nIf you eat yourself, you will die\n" \
                   "If you hit a wall you will die"
        super().__init__(screen_height, screen_width, gameHint)
        self.maze = Maze(screen_height, screen_width, self.display, 2)
        self.snake = SnakeGuy(self.display, self.snakeColor, self.maze.mazeRect)
        self.food = SnakeFood(self.maze.width, self.maze.height)
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

    def foodLayer(self):
        pygame.draw.rect(self.display, self.food_color, self.food.Rect)

    def eraseRect(self, squareRect):
            pygame.draw.rect(self.display, self.maze.mazeColor, squareRect)

    def checkLocation(self):
        # Checks if snake has crashed into wall or reached its destination:

        if self.food.x-9 <= self.snake.head.x <= (self.food.x+9):
            if self.food.y-9 <= self.snake.head.y <= (self.food.y+9):
                self.eraseRect(self.score.scoreBox)
                self.score.updateScore()
                if self.score.score == 10:
                    self.gameOver(True)
                else:
                    self.dropFood()
        else:
            for wall in self.maze.walls:
                if wall.x <= self.snake.head.x <= (wall.x + wall.width):
                    if wall.y <= self.snake.head.y <= (wall.y + wall.height):
                        self.gameOver()

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

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainLoop = False

pygame.init()
puzzle = SnakeGame2(800, 600)
puzzle.mainLoop()
pygame.quit()