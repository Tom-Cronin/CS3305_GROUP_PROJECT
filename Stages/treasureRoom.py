import pygame
from pygame.locals import *
import time
from Stages.baseStageClass import BaseStage, StageButton

class TreasureChestButton(StageButton): # Special button for the treasure box
    def __init__(self, announcement, screen_width, screen_height, bg_image):
        super().__init__("TREASURE", announcement, 0, 0)
        self.bgImage = bg_image
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.height = 300
        self.width = 400
        print(screen_width, screen_height)
        self.yLocation = ((screen_width - self.width) / 2) + 100
        self.xLocation = (screen_height - self.height) / 2
        self.image = (pygame.image.load("Stages/media/treasure_chest.png").convert_alpha()) # loads the treasure box as a png
        self.treasureImage = pygame.transform.scale(self.image, (self.width, self.height))

    def displayButton(self, display):
        display.blit(self.treasureImage, (self.xLocation, self.yLocation))


class TreasureRoom(BaseStage):
    def __init__(self, screen):
        self.screen_height = screen.screen_height
        self.screen_width = screen.screen_width

        #Generate prize
        self.prize = self.choosePrize()

        # init display screen
        self.display = screen.display
        self.bgImage = pygame.transform.scale(pygame.image.load('Stages/media/trees.png').convert(), (self.screen_height, self.screen_width))

        # Buttons
        self.quitGame = screen.quitGame
        self.treasureChest = TreasureChestButton("You have won " + self.prize + ".", self.screen_width,
                                                 self.screen_height, self.bgImage)
        self.okay = StageButton("OK", "", self.screen_height/2 - (self.quitGame.width + 50), self.screen_width/2)
        self.nevermind = StageButton("MAYBE NOT", "", self.screen_height/2 +50, self.screen_width/2)

        self.activeButtons = [self.quitGame, self.treasureChest]
        self.inactiveButtons = []
        self.selectedButtonName = None

        self.enabled = False  # allows the treasure chest button to be pressed

    def treasureLayer(self):
        self.treasureChest.displayButton(self.display)

    def mouseClick(self, button):  # event handler for button press
        if button.buttonText in ["QUIT", "SKIP", "BACK"]:
            self.selectedButtonName = self.warningMessage(button)
        elif button.buttonText in ["TREASURE"]:
            self.selectedButtonName = self.treasureMessage()
        elif button.buttonText == "OK":
            if self.selectedButtonName == "QUIT":
                self.exitGame()
            if self.selectedButtonName == "SKIP":
                self.skipStage()
            if self.selectedButtonName == "BACK":
                self.exitStage()
            if self.selectedButtonName == "TREASURE":
                self.openTreasure()
        elif button.buttonText == "MAYBE NOT":
            self.selectedButtonName = None
            self.enabled = False
            self.activeButtons = [self.quitGame, self.treasureChest]
            self.mainLoop()

    def choosePrize(self):
        # Todo: choose an attribute to increase, increase it, return prize name as string, chosen at random?
        return "nothing"

    def openTreasure(self):
        self.makeGreen()  # ToDo: exit map, give/save prize

    def treasureMessage(self):
        self.treasureChest.displayWarningMessage(self.display, self.screen_width, self.screen_height)
        self.displayButton(self.okay)
        time.sleep(0.3)
        self.activeButtons = [self.okay]  # deactivates the main menu and treasure box, activates ok option
        return self.treasureChest.buttonText

    def makeGreen(self):  # A filler function to end the stage
        green = (0, 255, 0)
        self.display.fill(green)
        pygame.display.update()
        self.activeButtons = [self.quitGame]
        self.selectedButtonName = None
        pygame.quit()
        exit(0)

    def mainLoop(self):  # listens for events

        self.backgroundLayer()
        self.treasureLayer()

        mainLoop = True

        while mainLoop:
            if self.enabled:
                self.listenMouse()
                self.listenButton()
            else:
                time.sleep(0.3)  # Delay before reactivating the treasure, to prevent accidental opening of chest
                self.enabled = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainLoop = False

# Can be uncommented For testing purposes but must be commented to stop overriding of main:
"""pygame.init()
s = BaseStage(1300, 700)
baseStage = TreasureRoom(s)
baseStage.mainLoop()
pygame.quit()"""

