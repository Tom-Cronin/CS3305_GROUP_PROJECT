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
        self.xLocation = (screen_width - self.width) / 2
        self.yLocation = (screen_height - self.height) / 2
        self.image = (pygame.image.load("media/treasure_chest.png").convert_alpha()) # loads the treasure box as a png
        self.treasureImage = pygame.transform.scale(self.image, (self.width, self.height))


    def displayButton(self, display):
        display.blit(self.treasureImage, (self.xLocation, self.yLocation))




class TreasureRoom(BaseStage):
    def __init__(self, screen_height, screen_width):
        super().__init__(screen_height, screen_width)
        self.prize = self.choosePrize()
        self.treasureChest = TreasureChestButton("You have won "+self.prize+".", screen_width, screen_height, self.bgImage)
        self.activeButtons.append(self.treasureChest)
        self.activeButtons.remove(self.goBack)


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

    def choosePrize(self):
        # Todo: choose an attribute to increase, increase it, return prize name as string, chosen at random?
        return "nothing"

    def openTreasure(self):
        self.makeGreen() # ToDo: exit map, give/save prize

    def treasureMessage(self):
        self.treasureChest.displayWarningMessage(self.display)
        self.displayButton(self.okay)
        time.sleep(0.3)
        self.activeButtons = [self.okay]  # deactivates the main menu and treasure box, activates ok option
        return self.treasureChest.buttonText

    def mainLoop(self):  # listens for events

        self.backgroundLayer()
        self.treasureLayer()

        mainLoop = True

        while mainLoop:
            self.listenMouse()
            self.listenButton()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainLoop = False


pygame.init()
baseStage = TreasureRoom(800, 600)
baseStage.mainLoop()
pygame.quit()