from Stages.baseStageClass import *
import time
from random import choice,randint

from Characters.enemyClasses import GateGuard,Hag,ShadowJest,Rat,Shadowling

class LoadingScreen:

    def __init__(self, screen,allies):
        # initializes the loading screen, as well as characters in the game for display purposes.
        self.baseScreen = screen
        self.font = 'Stages/media/Chapaza.ttf'
        self.fontsize = 20
        self.baseScreen = screen
        self.allylist = allies
        self.enemies = [GateGuard.GateGuard(), Hag.Hag(), ShadowJest.ShadowJest(), Rat.Rat(), Shadowling.Shadowling()]
        self.all = self.allylist + self.enemies
        self.baseScreen.default = pygame.transform.scale(
            pygame.image.load('Stages/media/paper.jpg').convert(),
            (self.baseScreen.screen_height, self.baseScreen.screen_width))
        self.baseScreen.end = pygame.transform.scale(
            pygame.image.load('Stages/media/MainMenueBackground2.png').convert(),
            (self.baseScreen.screen_height, self.baseScreen.screen_width))

    def backgroundLayer(self):
        # Draw white background padding for loading bar.
        pygame.draw.rect(self.baseScreen.display, (255, 255, 255), (292, 560, self.baseScreen.screen_height - 584, 30))
        pygame.draw.rect(self.baseScreen.display, (255, 255, 255), (310, 542, self.baseScreen.screen_height - 620, 66))
        pygame.draw.circle(self.baseScreen.display, (255, 255, 255), (310, 560), 18)
        pygame.draw.circle(self.baseScreen.display, (255, 255, 255), (self.baseScreen.screen_height - 310, 560), 18)
        pygame.draw.circle(self.baseScreen.display, (255, 255, 255), (310, 590), 18)
        pygame.draw.circle(self.baseScreen.display, (255, 255, 255), (self.baseScreen.screen_height - 310, 590), 18)

        # Draw grey background for loading bar.
        pygame.draw.rect(self.baseScreen.display, (120, 120, 120), (300, 560, self.baseScreen.screen_height - 600, 30))
        pygame.draw.rect(self.baseScreen.display, (120, 120, 120), (310, 550, self.baseScreen.screen_height - 620, 50))
        pygame.draw.circle(self.baseScreen.display, (120, 120, 120), (310, 560), 10)
        pygame.draw.circle(self.baseScreen.display, (120, 120, 120), (self.baseScreen.screen_height - 310, 560), 10)
        pygame.draw.circle(self.baseScreen.display, (120, 120, 120), (310, 590), 10)
        pygame.draw.circle(self.baseScreen.display, (120, 120, 120), (self.baseScreen.screen_height - 310, 590), 10)
        pygame.display.update()

    def drawInfo(self):
        # draws to the screen info about characters as well as the characters themselves

        self.baseScreen.display.blit(self.baseScreen.default, (0, 0))
        pygame.display.update()
        character = choice(self.all)
        image = pygame.image.load(character.imagePath).convert_alpha()
        oldScale = character.scale
        oldY = character.stagePositionY
        if character.isEnemy:
            image = pygame.transform.flip(image,True,False)
        if not character.isEnemy or character.name == "Rat" or character.name == "Shadowling":
            character.stagePositionY -= 280
            character.scale = ((character.scale[0])*2,(character.scale[1])*2)
        else:
            character.stagePositionY -= 40
        self.baseScreen.display.blit(
            pygame.transform.scale(image, character.scale),
            (200, character.stagePositionY))
        character.scale = oldScale
        character.stagePositionY = oldY

        self.drawCharDetails(character)



    def drawCharDetails(self,char):

        possitionY = 160

        font = pygame.font.Font(self.font, self.fontsize)
        name = font.render("Name: %s" % (char.name), True, (0, 0, 0))

        pygame.draw.rect(self.baseScreen.display, (0, 0, 0), (600, 52, 280, 75))
        pygame.draw.rect(self.baseScreen.display, (255, 255, 255), (605, 57, 270, 65))
        self.baseScreen.display.blit(name, (645, 68))

        name = font.render("Attacks: %i" % (len(char.allAttacks)), True, (0, 0, 0))

        pygame.draw.rect(self.baseScreen.display, (0, 0, 0), (900, 52, 280, 75))
        pygame.draw.rect(self.baseScreen.display, (255, 255, 255), (905, 57, 270, 65))
        self.baseScreen.display.blit(name, (945, 68))
        font = pygame.font.Font(self.font, self.fontsize- 4)
        for attack in char.allAttacks:
            name = font.render("%s" % (attack.name), True, (0, 0, 0))

            pygame.draw.rect(self.baseScreen.display, (0, 0, 0), (900, possitionY, 280, 60))
            pygame.draw.rect(self.baseScreen.display, (255, 255, 255), (905, possitionY + 5, 270, 50))
            self.baseScreen.display.blit(name, (945, possitionY + 16))
            font = pygame.font.Font(self.font, self.fontsize - 5)


            possitionY += 80


        pygame.display.update()

    def cleanUp(self):
        self.baseScreen.display.blit(self.baseScreen.end, (0, 0))
        pygame.display.update()

    def mainloop(self):
        self.drawInfo()
        self.backgroundLayer()

        i = 0
        bar_length = (self.baseScreen.screen_height - 600) / 200
        bar_jump = 199
        while i <= 199:
            pygame.draw.rect(self.baseScreen.display, (0, 191, 255), (300, 570, (self.baseScreen.screen_height - 600) - (bar_length * bar_jump), 10))
            pygame.display.update()
            i += 1
            bar_jump -= 1
            time.sleep(0.01)

