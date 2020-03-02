import pygame
from pygame.locals import *
import time
from random import choice,randint
from Stages.baseStageClass import BaseStage, StageButton

class TreasureChestButton(StageButton): # Special button for the treasure box
    def __init__(self, announcement, screen_width, screen_height):
        super().__init__("TREASURE", announcement, 0, 0)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.height = 300
        self.width = 400
        self.yLocation = ((screen_width - self.width) / 2) + 100
        self.xLocation = (screen_height - self.height) / 2
        self.image = (pygame.image.load("Stages/media/treasure_chest.png").convert_alpha()) # loads the treasure box as a png
        self.treasureImage = pygame.transform.scale(self.image, (self.width, self.height))

    def displayButton(self, display):
        display.blit(self.treasureImage, (self.xLocation, self.yLocation))


class TreasureRoom(BaseStage):
    def __init__(self, screen, team):
        self.screen_height = screen.screen_height
        self.screen_width = screen.screen_width
        self.team = team
        #Generate prize
        self.prize = self.generatePrize()


        # init display screen
        self.display = screen.display
        self.bgImage = pygame.transform.scale(pygame.image.load('Stages/media/MainMenueBackground.png').convert(), (self.screen_height, self.screen_width))

        # Buttons
        self.quitGame = screen.quitGame
        self.treasureChest = TreasureChestButton("You found a twisted charm, " + self.prize + ".", self.screen_width,
                                                 self.screen_height)
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

    def generatePrize(self):  # ToDo: a general prize generator to be called by each room/stage?
        char = choice(self.team)
        increaseAmount = randint(1, 4)
        att = choice(["strength",
                      "dexterity",
                      "constitution",
                      "intelligence"])
        char.levelUp(att, increaseAmount)
        return "%s's\n %s increased by %i" % (char.name, att, increaseAmount)

    def openTreasure(self):
        return 1

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
                if (self.listenMouse()):
                    return 1
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
from Characters.playerClasses.warlock import Warlock
from Characters.playerClasses.fighter import Fighter
from Characters.playerClasses.oldLady import OldLady
from Characters.playerClasses.healer import Healer
team = [Warlock(), Fighter(), OldLady(), Healer()]
baseStage = TreasureRoom(s, team)
baseStage.mainLoop()
pygame.quit()"""
