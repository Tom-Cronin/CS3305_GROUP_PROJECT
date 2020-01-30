import pygame
from pygame.locals import *
from Stages.baseStageClass import *

class MainMenu:

    def __init__(self, screen_height, screen_width):
        self.baseScreen = BaseStage(screen_height, screen_width)
        self.baseScreen.bgImage = pygame.transform.scale(pygame.image.load('media/MainMenueBackground.png').convert(),
                                                         (self.baseScreen.screen_height, self.baseScreen.screen_width))

        #buttons
        self.height = screen_width
        self.width = screen_height
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
            pygame.quit()
            quit(0)
        if button.buttonText == "Go Back":
            self.activeButtons = [self.startGameButton, self.quitButton]
            self.mainLoop()
        if button.buttonText == "Start Game":
            pass #to do when map is here

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
                    self.mouseClick(button)

            else:
                button.hover(self.baseScreen.display, False)
            updateRect = Rect(button.xLocation, button.yLocation, button.width, button.height)
            pygame.display.update(updateRect)


    def mainLoop(self):  # listens for events
        self.backgroundLayer()

        mainLoop = True
        while (mainLoop):
            self.listenMouse()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainLoop = False

pygame.init()
mainMenu = MainMenu(1300, 700)
mainMenu.mainLoop()
pygame.quit()