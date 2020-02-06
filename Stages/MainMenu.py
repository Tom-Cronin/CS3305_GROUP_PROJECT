import pygame
from pygame.locals import *
from Stages.baseStageClass import *
import time

class MainMenu:

    def __init__(self, screen):
        self.baseScreen = screen
        self.baseScreen.bgImage = pygame.transform.scale(pygame.image.load('Stages/media/MainMenueBackground.png').convert(),
                                                         (self.baseScreen.screen_height, self.baseScreen.screen_width))

        #buttons
        self.height = self.baseScreen.screen_width
        self.width = self.baseScreen.screen_height
        self.startGameButton = StageButton("Start Game", "", self.width/4, self.height/3.5)
        self.quitButton = StageButton("Quit Game", "", self.width/4, self.height/1.65)
        self.leaveButton = StageButton("Quit", "", self.width/1.6, self.height/1.2)
        self.noButton = StageButton("Go Back", "", self.width/6.4, self.height/1.2)
        self.activeButtons = [self.startGameButton, self.quitButton]
        self.allbuttons = [self.startGameButton, self.quitButton, self.leaveButton, self.noButton]
        for button in self.allbuttons:
            button.defaultColour = (120,120,120)
            button.textColor = (102, 51, 0)
            button.hovercolour = (40, 40, 40)
        self.startGameButton.height = 100
        self.startGameButton.width = self.width/2
        self.quitButton.height = self.startGameButton.height
        self.quitButton.width = self.startGameButton.width
        self.leaveButton.height = self.startGameButton.height
        self.leaveButton.width = 300
        self.noButton.height = self.startGameButton.height
        self.noButton.width = self.leaveButton.width

    def backgroundLayer(self):
        self.baseScreen.display.blit(self.baseScreen.bgImage, (0, 0))
        for button in self.activeButtons:
            self.baseScreen.displayButton(button)
        pygame.display.update()

    def mouseClick(self, button):
        if button.buttonText == "Quit Game":
            self.quitting()
        if button.buttonText == "Quit":
            return False
        if button.buttonText == "Go Back":
            self.activeButtons = [self.startGameButton, self.quitButton]
            self.mainLoop()
        if button.buttonText == "Start Game":
            return True

    def quitting(self):
        self.baseScreen.displayButton(self.leaveButton)
        self.baseScreen.displayButton(self.noButton)
        self.activeButtons = [self.leaveButton, self.noButton]

    def listenMouse(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for button in self.activeButtons:
            if (button.xLocation + button.width) > mouse[0] > button.xLocation and (
                    button.yLocation + button.height) > mouse[1] > button.yLocation:
                button.hover(self.baseScreen.display, True)
                if click[0] == 1:
                    if self.mouseClick(button) == False:
                        return False
                    elif self.mouseClick(button) == True:
                        return True
                    else:
                        return 10

            else:
                button.hover(self.baseScreen.display, False)
            updateRect = Rect(button.xLocation, button.yLocation, button.width, button.height)
            pygame.display.update(updateRect)


    def mainLoop(self):  # listens for events
        self.backgroundLayer()

        mainLoop = True
        while (mainLoop):
            listening = self.listenMouse()
            if listening == False:
                return False
            elif listening == True:
                return True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainLoop = False