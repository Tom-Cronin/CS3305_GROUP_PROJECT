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
        self.x = random.randint(10, self.maze_height-10)
        self.y = random.randint(10, self.maze_width - 10)
        self.Rect = Rect((self.x, self.y, self.size, self.size))


class SnakeGame1(SnakeGame):

    def __init__(self, screen_height, screen_width):
        gameHint = "Eat 10 squares\nUse the arrow keys to move\nIf you eat yourself, you will die\n" \
                   "If you hit a wall you will die"
        super().__init__(screen_height, screen_width, gameHint)
        self.maze = Maze(screen_height, screen_width, self.display, 2)
        self.snake = SnakeGuy(self.display, self.snakeColor, self.maze.mazeRect)
        self.food = SnakeFood(self.maze.width, self.maze.height)
        self.food_color = (0, 0, 0)  # black
        self.snake.move("R")
        self.snake.move("R")
        self.snake.move("R")  # This technically solves the moving/snake image break at the start of the game

    def listenSnake(self):
        # Checks if snake should move:
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.snake.move("U")
            self.checkLocation()
        elif key[pygame.K_DOWN]:
            self.snake.move("D")
            self.checkLocation()
        elif key[pygame.K_RIGHT]:
            self.snake.move("R")
            self.checkLocation()
        elif key[pygame.K_LEFT]:
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

    def foodLayer(self):
        pygame.draw.rect(self.display, self.food_color, self.food.Rect)
        print("Food")
        #pygame.display.update(self.food.Rect)

    def eraseRect(self, squareRect):
            pygame.draw.rect(self.display, self.maze.mazeColor, squareRect)


    def checkLocation(self):
        # Checks if snake has crashed into wall or reached its destination:
        if self.food.x <= self.snake.head.x <= (self.food.x+10):
            if self.food.y <= self.snake.head.y <= (self.food.y + 10):
                self.gameOver(True)
        else:
            for wall in self.maze.walls:
                if wall.x <= self.snake.head.x <= (wall.x + wall.width-10):
                    if wall.y <= self.snake.head.y <= (wall.y + wall.height-10):
                        self.gameOver()

    def mainLoop(self):  # listens for events

        self.backgroundLayer()
        self.mazeLayer()
        self.foodLayer()
        self.snakeLayer()



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
puzzle = SnakeGame1(800, 600)
puzzle.mainLoop()
pygame.quit()