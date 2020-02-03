import pygame, sys
from pygame.locals import *

from Stages.baseStageClass import *

class EncounterStage():
    def __init__(self, screen_height, screen_width):
        self.display_width = screen_width
        self.display_height = screen_height
        self.white = (255,255,255)

        self.gameDisplay = pygame.display.set_mode((self.display_height, self.display_width))
        self.bgImage = pygame.transform.scale(pygame.image.load('media/MainMenueBackground.png').convert(),
                                                         (self.display_height, self.display_width))
        self.gameDisplay.fill(self.white)

    def displayBox(self):
        pygame.draw.rect(self.gameDisplay, (120, 120, 120), (self.display_width/4, self.display_height/3.5, self.display_width, self.display_height))  # border
        # pygame.draw.rect(display, self.bgColour,
        #                  (self.xLocation + 5, self.yLocation + 5, self.width - 10, self.height - 10))
        # text = self.buttonText
        # font = pygame.font.Font(self.font, self.fontsize)
        # text = font.render(text, True, self.textColor)
        # textRect = text.get_rect()
        # textRect.center = ((self.xLocation + (self.width / 2)), self.yLocation + (self.height / 2))
        # display.blit(text, textRect)

    def mainLoop(self):  # listens for events
        self.displayBox()

        mainLoop = True
        while (mainLoop):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainLoop = False


pygame.init()
mainMenu = EncounterStage(1300, 700)
mainMenu.mainLoop()
pygame.quit()