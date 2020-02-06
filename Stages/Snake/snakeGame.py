from Stages.baseStageClass import BaseStage
from Stages.Snake.snakeMaze import Maze
from Stages.Snake.snakeSnake import SnakeGuy
import pygame
import time

class SnakeGame(BaseStage):

    def __init__(self, screen_height, screen_width):

        super().__init__(screen_height, screen_width)
        self.activeButtons = [self.quitGame]
        self.snakeColor = (0, 0, 0)  # black
        self.wallColor = (0, 0, 0)  # black
        self.textColor = (0, 0, 0)
        self.font = 'media/Chapaza.ttf'
        self.maze = Maze(screen_height, screen_width, self.display)
        self.snake = SnakeGuy(self.display, self.snakeColor, self.maze.mazeRect)
        self.finished = False


    def mazeLayer(self):
        self.maze.draw()

    def snakeLayer(self):
        self.snake.draw()

    def generatePrize(self):  # ToDo: a general prize generator to be called by each room/stage?
        return "nothing"

    def gameOver(self, win=False):  # ends the game when a win/failure occurs
        self.finished = True
        self.maze.drawBackground()
        if win is False:
            message = "You lost!\nGame over"
        else:
            prize = self.generatePrize()
            message = "Congrats!\nYou win "+prize
        self.activeButtons = [self.okay]
        self.okay.yLocation += 100
        self.okay.displayButton(self.display)
        y = self.screen_width/2
        for line in message.split('\n'):  # allows for multiple-line output
            font = pygame.font.Font(self.font, 40)
            text = font.render(line, True, self.textColor)
            textRect = text.get_rect()
            textRect.center = (self.screen_height/2, y)
            y += 50
            self.display.blit(text, textRect)
            self.selectedButtonName = "ENDGAME"
        pygame.display.update()

    def mouseClick(self, button):  # event handler for button press
        if button.buttonText in ["QUIT", "SKIP", "BACK"]:
            self.selectedButtonName = self.warningMessage(button)
        if button.buttonText == "MAYBE NOT":
            self.neverMind()
        if button.buttonText == "OK":
            if self.selectedButtonName == "QUIT":
                self.exitGame()
            if self.selectedButtonName == "SKIP":
                self.skipStage()
            if self.selectedButtonName == "BACK":
                self.exitStage()
            if self.selectedButtonName == "ENDGAME":
                self.continueGame()

    def listenSnake(self):
        # Checks if snake should move:
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            #ToDo: if in limits...
            self.snake.move("Up")
            self.checkLocation()
        elif key[pygame.K_DOWN]:
            self.snake.move("Down")
            self.checkLocation()
        elif key[pygame.K_RIGHT]:
            self.snake.move("Right")
            self.checkLocation()

        elif key[pygame.K_LEFT]:
            self.snake.move("Left")
            self.checkLocation()

        time.sleep(0.1)

    def checkLocation(self):
        # Checks if snake has crashed into wall or reached its destination:
        """print(self.snake.head.x, self.maze.exit.x)
        print(self.snake.head.y, self.maze.exit.y,"-", self.maze.exit.y + self.maze.exit.height)
        print("***********")"""
        if self.maze.exit.x == self.snake.head.x and  self.maze.exit.y <= self.snake.head.y <= (self.maze.exit.y + self.maze.exit.height):
            self.gameOver(True)
        else:
            for wall in self.maze.walls:
                """if wall.x <= self.snake.head.x < wall.x + wall.width:
                    if wall.y <= self.snake.head.y <= wall.y + wall.width:"""
                if wall.x <= self.snake.head.x <= (wall.x + wall.width-10):
                    if wall.y <= self.snake.head.y <= (wall.y + wall.height-10):
                        print("y")
                        self.gameOver()

    def continueGame(self):
        self.makeGreen()
        # ToDo: return to map


    def mainLoop(self):  # listens for events

        self.backgroundLayer()
        self.mazeLayer()
        self.snakeLayer()
        #self.gameOver(True)

        pygame.display.update()
        #time.sleep(5)

        mainLoop = True

        while mainLoop:
            self.listenMouse()
            self.listenButton()
            if self.finished is False:
                self.listenSnake()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainLoop = False



pygame.init()
puzzle = SnakeGame(800, 600)
puzzle.mainLoop()
pygame.quit()