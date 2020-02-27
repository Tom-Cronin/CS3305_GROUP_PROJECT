from Stages.baseStageClass import BaseStage, StageButton
from Stages.Snake.snakeMaze import Maze
from Stages.Snake.snakeSnake import SnakeGuy
import pygame
from pygame.locals import *
import time

class SnakeGame(BaseStage):

    def __init__(self, screen, hint):
        # init display screen
        self.screen_height = screen.screen_height
        self.screen_width = screen.screen_width
        self.display = screen.display

        # Buttons
        self.quitGame = screen.quitGame
        self.okay = screen.okay
        self.nevermind = screen.nevermind

        self.inactiveButtons = []  # buttons that are visible but deactivated
        self.selectedButtonName = None

        self.bgImage = pygame.transform.scale(pygame.image.load('Stages/media/trees.png').convert(),
                                              (self.screen_height, self.screen_width))

        self.disabled = False  # snake movement is disabled while message is displayed
        self.snakeColor = (0, 0, 0)  # black
        self.wallColor = (0, 0, 0)  # black
        self.textColor = (0, 0, 0)
        self.font = 'Stages/media/Chapaza.ttf'
        self.maze = Maze(self.screen_height, self.screen_width, self.display)
        self.snake = SnakeGuy(self.display, self.snakeColor, self.maze)
        self.finished = False
        self.hint = StageButton("HINT", hint, screen.goBack.xLocation, screen.goBack.yLocation)
        self.activeButtons = [self.quitGame, self.hint]


    def mazeLayer(self):
        self.maze.draw()

    def snakeLayer(self):
        self.snake.draw()

    def generatePrize(self):  # ToDo: a general prize generator to be called by each room/stage?
        return "nothing"

    def gameOver(self, win=False):  # ends the game when a win/failure occurs
        self.finished = True
        updateRect = Rect((self.screen_height/4, self.screen_width/4, self.screen_height/2, self.screen_width/2))
        pygame.draw.rect(self.display, self.okay.textColor, updateRect)  # border
        pygame.draw.rect(self.display, self.textColor, (self.screen_height/4 + 5, self.screen_width/4 + 5,
                                                   self.screen_height/2 - 10, self.screen_width/2 - 10))
        if win is False:
            message = "You lost!\nGame over"
        else:
            prize = self.generatePrize()
            message = "Congrats!\nYou win "+prize
        self.activeButtons = [self.okay]
        self.okay.yLocation += 100
        self.okay.displayButton(self.display)
        y = self.screen_width/4 + 50
        for line in message.split('\n'):  # allows for multiple-line output
            font = pygame.font.Font(self.font, 40)
            text = font.render(line, True, (self.okay.textColor))
            textRect = text.get_rect()
            textRect.center = (self.screen_height/2, y)
            y += 50
            self.display.blit(text, textRect)
            self.selectedButtonName = "ENDGAME"
        pygame.display.update()

    def mouseClick(self, button):  # event handler for button press
        self.disabled = True
        if button.buttonText in ["QUIT", "SKIP", "BACK"]:
            self.selectedButtonName = self.warningMessage(button)
        if button.buttonText == "HINT":
            self.howToPlay()
            self.selectedButtonName = "HINT"
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
            if self.selectedButtonName == "HINT":
                self.neverMind()

    def neverMind(self):  # Resets the basic Stage background
        self.disabled = False
        self.activeButtons = [self.quitGame, self.hint]
        self.selectedButtonName = None
        self.mainLoop()

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

    def checkLocation(self):
        # Checks if snake has crashed into wall or reached its destination:
        if self.maze.exit.x == self.snake.head.x and  self.maze.exit.y <= self.snake.head.y <= (self.maze.exit.y + self.maze.exit.height):
            self.gameOver(True)
        else:
            for wall in self.maze.walls:
                if wall.x <= self.snake.head.x <= (wall.x + wall.width-10):
                    if wall.y <= self.snake.head.y <= (wall.y + wall.height-10):
                        self.gameOver()

    def continueGame(self):
            green = (0, 255, 0)
            self.display.fill(green)
            pygame.display.update()
            self.selectedButtonName = None
            pygame.quit()
            exit(0)
        # ToDo: return to map

    def howToPlay(self):
        self.hint.displayWarningMessage(self.display, self.screen_width, self.screen_height)
        self.displayButton(self.okay)
        time.sleep(0.3)
        self.activeButtons = [self.okay]  # deactivates the main menu and treasure box, activates ok option
        return self.hint.buttonText


    def mainLoop(self):  # listens for events

        self.backgroundLayer()
        self.mazeLayer()
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
