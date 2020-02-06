import pygame, sys
from pygame.locals import *

from Stages.baseStageClass import *
from CombatSystem.combat import *




class EncounterStage():
    def __init__(self, screen_height, screen_width, level):
        self.display_width = screen_width
        self.display_height = screen_height
        self.defaultColour = (120, 120, 120)

        self.attack1 = StageButton("ATTACK1", "", 100, 485)
        self.attack1.height = 200
        self.attack2 = StageButton("ATTACK2", "", 380, 485)
        self.attack2.height = 200
        self.attack3 = StageButton("ATTACK3", "", 660, 485)
        self.attack3.height = 200
        self.attack4 = StageButton("ATTACK4", "", 940, 485)
        self.attack4.height = 200
        self.allbuttons = [self.attack1, self.attack2, self.attack3, self.attack4]
        for button in self.allbuttons:
            button.defaultColour = (255,255,255)
            button.textColor = (102, 51, 0)
            button.hovercolour = (200, 200, 200)
        self.base = BaseStage(self.display_height, self.display_width)
        self.base.bgImage = pygame.transform.scale(pygame.image.load(level).convert(), (self.display_height, self.display_width))
        pygame.display.update()

        setUp(4, [Warlock(), Warlock(), Warlock(), Warlock()])

        self.turnOrder =

        self.enemies = []

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

    def listenMouse(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for button in self.allbuttons:
            if (button.xLocation + button.width) > mouse[0] > button.xLocation and (
                    button.yLocation + button.height) > mouse[1] > button.yLocation:
                button.hover(self.base.display, True)
                if click[0] == 1:
                    self.mouseClick(button)
            else:
                button.hover(self.base.display, False)
            updateRect = Rect(button.xLocation, button.yLocation, button.width, button.height)
            pygame.display.update(updateRect)

    def mainLoop(self):  # listens for events
        self.displayBattle()

        mainLoop = True
        while (mainLoop):
            self.listenMouse()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainLoop = False


pygame.init()
mainMenu = EncounterStage(1300, 700, "media/MainMenueBackground.png")
mainMenu.mainLoop()
pygame.quit()