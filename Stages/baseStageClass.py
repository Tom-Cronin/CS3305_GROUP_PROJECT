import pygame, sys
import textwrap
from pygame.locals import *

#pygame.init()

class StageButton:
    def __init__(self, text, exitMessage, x, y):
        self.buttonText = text
        self.bgColour = (255, 255, 255)
        self.width = 200
        self.height = 100
        self.xLocation = x
        self.yLocation = y
        self.textColor = (0, 255, 0)
        self.font = 'media/Chapaza.ttf'
        self.fontsize = 30
        self.exitMessage = exitMessage # Message displayed when button is pressed

    def displayButton(self, display):
        pygame.draw.rect(display, self.textColor, (self.xLocation, self.yLocation, self.width, self.height))  # border
        pygame.draw.rect(display, self.bgColour, (self.xLocation+5, self.yLocation+5, self.width-10, self.height-10))
        text = self.buttonText
        font = pygame.font.Font(self.font, self.fontsize)
        text = font.render(text, True, self.textColor)
        textRect = text.get_rect()
        textRect.center = ((self.xLocation+(self.width/2)), self.yLocation+(self.height/2))
        display.blit(text, textRect)

    def displayWarningMessage(self, display):
        pygame.draw.rect(display, self.textColor, (200, 150, 500, 300)) # border
        pygame.draw.rect(display, self.bgColour, (205, 155, 490, 290))
        y = 200
        for line in self.exitMessage.split('\n'): # allows for multiple-line output
            font = pygame.font.Font(self.font, 20)
            text = font.render(line, True, self.textColor)
            textRect = text.get_rect()
            textRect.center = (450, y)
            y += 50
            display.blit(text, textRect)

    def hover(self, display, hover):
        if hover is True:
            self.bgColour = (0, 0, 0)
            self.displayButton(display)
        else:
            self.bgColour = (255, 255, 255)
            self.displayButton(display)

class BaseStage():
    #bgColour = (0, 0, 0)
    bgImage = 'media/trees.png'

    # Buttons
    quitGame = StageButton("QUIT", "Are you sure you want to quit the game?\nYour data will not be saved", 10, 10)
    goBack = StageButton("BACK", "Are you sure you want to leave?\nYour data will not be saved", 300, 10)
    skip = StageButton("SKIP", "Are you sure you want to skip?\nYou will not gain any rewards from this stage", 600, 10)
    okay = StageButton("OK", "", (490 / 2) - 20, 450 - 100)
    nevermind = StageButton("MAYBE NOT", "", 490 - 20, 450 - 100)

    activeButtons = [quitGame, goBack, skip]
    selectedButtonName = None
    
    def displayButton(self, display, button): # ToDo: optional disabled arg ?
        button.displayButton(display)

    def warningMessage(self, display, button):
        # Warning message is displayed when the player attempts to leave the stage
        button.displayWarningMessage(display)
        self.displayButton(display, self.okay)
        self.displayButton(display, self.nevermind)
        self.activeButtons = [self.okay, self.nevermind]  # deactivates the main menu, activates ok and nm options
        return button.buttonText

    def listen(self, display):  # listens for hovering/clicking of buttons
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for button in self.activeButtons:
            if (button.xLocation + button.width) > mouse[0] > button.xLocation and (
                    button.yLocation + button.height) > mouse[1] > button.yLocation:
                button.hover(display, True)
                if click[0] == 1:
                    self.buttonClick(display, button)
            else:
                button.hover(display, False)

    def buttonClick(self, display, button):  # event handler for button press
        if button.buttonText in ["QUIT", "SKIP", "BACK"]:
            self.selectedButtonName = self.warningMessage(display, button)
        if button.buttonText == "MAYBE NOT":
            self.neverMind(display)
        if button.buttonText == "OK":
            if self.selectedButtonName == "QUIT":
                self.exitGame(display)
            if self.selectedButtonName == "SKIP":
                self.skipStage(display)
            if self.selectedButtonName == "BACK":
                self.exitStage(display)
            else:
                pass  # ToDo: Error Message?

    def exitGame(self, display):  # ToDo: Exit to main menu
        self.makeGreen(display)

    def skipStage(self, display):  # ToDo: Exit to map, map node skipped
        self.makeGreen(display)

    def exitStage(self, display):  # i.e. goBack # ToDo: Exit to map, map node 'unentered'
        self.makeGreen(display)

    def neverMind(self, display):  # Resets the basic Stage background ToDo: Layers?
        self.displayButton(display, self.quitGame)
        self.displayButton(display, self.goBack)
        self.displayButton(display, self.skip)
        display.blit(pygame.image.load('media/trees.png'), (0, 0))
        self.activeButtons = [self.quitGame, self.goBack, self.skip]
        self.selectedButtonName = None

    def makeGreen(self, display):  # A filler function to end the stage
        green = (0, 255, 0)
        display.blit(pygame.image.load('media/trees.png'), (0, 0))
        display.fill(green)
        pygame.display.update()
        self.activeButtons = [self.quitGame, self.goBack, self.skip]
        self.selectedButtonName = None
        pygame.quit()

