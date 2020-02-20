from Stages.Snake.snakeMaze import Maze
from Stages.Snake.snakeSnake import SnakeGuy
from Stages.Snake.snakeGame import SnakeGame
import pygame


class SnakeGame1(SnakeGame):

    def __init__(self, screen_height, screen_width):
        gameHint = "Try and get the snake to the end of the maze\nUse the arrow keys to move\n" \
                   "If you hit a wall, you will die"
        super().__init__(screen_height, screen_width, gameHint)
        self.maze = Maze(screen_height, screen_width, self.display)
        self.snake = SnakeGuy(self.display, self.snakeColor, self.maze.mazeRect)
        self.snake.move("R")
        self.snake.move("R")
        self.snake.move("R")  # This technically solves the moving/snake image break at the start of the game

pygame.init()
puzzle = SnakeGame1(800, 600)
puzzle.mainLoop()
pygame.quit()