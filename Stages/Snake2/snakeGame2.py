from Stages.baseStageClass import BaseStage, StageButton
from Stages.Snake.snakeMaze import Maze
from Stages.Snake.snakeSnake import SnakeGuy
from Stages.Snake.snakeGame import SnakeGame
import pygame
import time

class SnakeGame1(SnakeGame):

    def __init__(self, screen_height, screen_width):
        gameHint = "Eat\nUse the arrow keys to move\nIf you eat yourself, you will die\nIf you hit a wall you will die"
        super().__init__(screen_height, screen_width, gameHint)
        self.maze = Maze(screen_height, screen_width, self.display)
        self.snake = SnakeGuy(self.display, self.snakeColor, self.maze.mazeRect)

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

pygame.init()
puzzle = SnakeGame1(800, 600)
puzzle.mainLoop()
pygame.quit()