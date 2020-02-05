import pygame, sys
from pygame.locals import *

from Stages.baseStageClass import *

class EncounterStage():
    def __init__(self, screen_height, screen_width, level):
        self.display_width = screen_width
        self.display_height = screen_height
        self.defaultColour = (120, 120, 120)
        self.hoverColour = (40, 40, 40)
        self.textColour = (102, 51, 0)

        self.quitGame = StageButton("ATTACK1", "Are you sure you want to quit the game?\nYour data will not be saved", 20,
                                    485)
        self.quitGame.height = 200
        self.goBack = StageButton("ATTACK2", "Are you sure you want to leave?\nYour data will not be saved", 300, 485)
        self.goBack.height = 200
        self.skip = StageButton("ATTACK3", "Are you sure you want to skip?\nYou will not gain any rewards from this stage",
                                580, 485)
        self.skip.height = 200
        self.okay = StageButton("ATTACK4", "", 860, 485)
        self.okay.height = 200
        self.allbuttons = [self.quitGame, self.goBack, self.okay, self.skip]
        for button in self.allbuttons:
            button.defaultColour = (120,120,120)
            button.textColor = (102, 51, 0)
            button.hovercolour = (40, 40, 40)
        self.base = BaseStage(self.display_height, self.display_width)
        self.base.bgImage = pygame.transform.scale(pygame.image.load(level).convert(), (self.display_height, self.display_width))
        pygame.display.update()
    def displayBattle(self):
        self.base.display.blit(self.base.bgImage, (0, 0))
        pygame.draw.rect(self.base.display, self.defaultColour, (self.display_width/300, self.display_width/1.5, self.display_width*1.9, self.display_height))  # border
        for button in self.allbuttons:
            self.base.displayButton(button)
        pygame.display.update()
        # pygame.draw.rect(display, self.bgColour,
        #                  (self.xLocation + 5, self.yLocation + 5, self.width - 10, self.height - 10))
        # text = self.buttonText
        # font = pygame.font.Font(self.font, self.fontsize)
        # text = font.render(text, True, self.textColor)
        # textRect = text.get_rect()
        # textRect.center = ((self.xLocation + (self.width / 2)), self.yLocation + (self.height / 2))
        # display.blit(text, textRect)

    def mainLoop(self):  # listens for events
        self.displayBattle()

        mainLoop = True
        while (mainLoop):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainLoop = False


pygame.init()
mainMenu = EncounterStage(1300, 700, "media/MainMenueBackground.png")
mainMenu.mainLoop()
pygame.quit()