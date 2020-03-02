from Stages.Snake.snakeMaze import Maze
from Stages.Snake.snakeSnake import SnakeGuy
from Stages.Snake.snakeGame import SnakeGame
from Stages.baseStageClass import BaseStage
import pygame


class SnakeGame1(SnakeGame):

    def __init__(self, screen):
        gameHint = "Try and get the snake to the end of the maze\nUse the arrow keys to move\n" \
                   "If you hit a wall, you will die"
        super().__init__(screen, gameHint)
        self.maze = Maze(screen.screen_height, screen.screen_width, self.display)
        self.snake = SnakeGuy(self.display, self.snakeColor, self.maze)
        self.snake.move("R")
        self.snake.move("R")
        self.snake.move("R")  # This technically solves the moving/snake image break at the start of the game

# Can be uncommented For testing purposes but must be commented to stop overriding of main:
"""pygame.init()
s = BaseStage(1300, 700)
puzzle = SnakeGame1(s)
puzzle.mainLoop()
pygame.quit()"""
