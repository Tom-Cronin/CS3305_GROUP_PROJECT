import pygame, sys, os
from pygame.locals import *

from Stages.baseStageClass import *
from CombatSystem.combat import *


class EncounterStage():
    def __init__(self, screen_height, screen_width, levelImage, crLevel, listOfPlayers):
        self.display_width = screen_width
        self.display_height = screen_height
        self.defaultColour = (120, 120, 120)
        self.white = (255, 255, 255)
        self.font = '../Stages/media/Chapaza.ttf'
        self.fontsize = 20
        self.enemy = None
        self.enemyToPick = False
        self.attack = None
        self.attackToPick = False

        self.attack1 = StageButton("ATTACK1", "", 25, 592)
        self.attack1.height = 50
        self.attack2 = StageButton("ATTACK2", "", 25, 642)
        self.attack2.height = 50
        self.attack3 = StageButton("ATTACK3", "", 225, 592)
        self.attack3.height = 50
        self.attack4 = StageButton("ATTACK4", "", 225, 642)
        self.attack4.height = 50
        self.allbuttons = [self.attack1, self.attack2, self.attack3, self.attack4]
        for button in self.allbuttons:
            button.defaultColour = (155, 155, 155)
            button.textColor = (102, 51, 0)
            button.hovercolour = (155, 155, 155)
        self.base = BaseStage(self.display_height, self.display_width)
        self.base.bgImage = pygame.transform.scale(pygame.image.load(levelImage).convert(), (self.display_height, self.display_width))
        pygame.display.update()

        self.combatBoard = pygame.transform.scale(pygame.image.load("media/combatBoard.png").convert_alpha(), (1300, 400))

        self.displayBattle()

        self.combat = combatEncounter()
        self.combat.setUp(crLevel, listOfPlayers)
        self.turnOrder = self.combat.turnOrder
        self.displayCharacter()

        self.mainLoop()

        self.enemies = []

    def displayBattle(self):
        self.base.display.blit(self.base.bgImage, (0, 0))
        self.base.display.blit(self.combatBoard, (0, 300))
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

    def displayHealth(self, character, position):
        health = str(character.health) + "/" + str(character.maxHealth)
        font = pygame.font.Font(self.font, self.fontsize)
        text = font.render(health, True, self.white, (102, 51, 0))
        if character.isEnemy:
            self.base.display.blit(text, (position + 100, 175))
        else:
            self.base.display.blit(text, (position + 100, 175))

    def displayCharacter(self):
        positionEnemy = 600
        positionAlly = -80
        for character in self.turnOrder:
            if character.isEnemy:
                self.base.display.blit(pygame.transform.scale(pygame.image.load(character.imagePath).convert_alpha(), (330, 330)), (positionEnemy, 200))
                self.displayHealth(character, positionEnemy)
                positionEnemy += 150
            else:
                self.attack1 = StageButton(character.attack_slot_1.name, "attack 0", 25, 592)
                self.attack1.height = 50
                self.attack1.fontsize = 20
                self.attack2 = StageButton(character.attack_slot_2.name, "attack 1", 25, 642)
                self.attack2.height = 50
                self.attack2.fontsize = 20
                self.attack3 = StageButton(character.attack_slot_3.name, "attack 2", 225, 592)
                self.attack3.height = 50
                self.attack3.fontsize = 20
                self.attack4 = StageButton(character.attack_slot_4.name, "attack 3", 225, 642)
                self.attack4.height = 50
                self.attack4.fontsize = 20

                self.e1 = StageButton("Enemy 1", "e 0", 625, 592)
                self.e1.height = 50
                self.e1.fontsize = 20
                self.e2 = StageButton("Enemy 2", "e 1", 625, 642)
                self.e2.height = 50
                self.e2.fontsize = 20
                self.e3 = StageButton("Enemy 3", "e 2", 825, 592)
                self.e3.height = 50
                self.e3.fontsize = 20
                self.e4 = StageButton("Enemy 4", "e 3", 825, 642)
                self.e4.height = 50
                self.e4.fontsize = 20
                self.allbuttons = [self.attack1, self.attack2, self.attack3, self.attack4, self.e1, self.e2, self.e3, self.e4]
                for button in self.allbuttons:
                    button.defaultColour = (255, 255, 255)
                    button.textColor = (0, 0, 0)
                    button.hovercolour = (200, 200, 200)
                self.base.display.blit(pygame.transform.scale(pygame.image.load(character.imagePath).convert_alpha(), (330, 330)), (positionAlly, 200))
                self.displayHealth(character, positionAlly)
                positionAlly += 150
        pygame.display.update()

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

    def goThrougheachTurn(self, combatEncounterInstance):
        count = 0
        clicked = False
        while len(combatEncounterInstance.enemies) > 0 and len(combatEncounterInstance.allies) > 0:
            for character in combatEncounterInstance.turnOrder:
                if character.isEnemy:
                    combatEncounterInstance.calcDamage(makeMove(character, combatEncounterInstance.allies))
                else:
                    while clicked == False:
                        for event in pygame.event.get():
                            self.listenMouse()
                            if self.enemyToPick == True and self.attackToPick == True:
                                clicked = True
                    character.allAttacks[self.attack].startCooldown()
                    combatEncounterInstance.calcDamage([character.allAttacks[self.attack].getDamage(),combatEncounterInstance.enemies[self.enemy]] , character)
                    clicked = False
                    self.attackToPick = False
                    self.enemyToPick = False
                for attack in character.allAttacks:
                    attack.reduceCoolDown()
            count += 1

        if len(combatEncounterInstance.enemies) <= 0:
            print("Allys won\n\n")
        else:
            print("Enemys won\n\n")
        print(count)


    def mouseClick(self, button):
        messageType, number = button.exitMessage.split()[0], button.exitMessage.split()[1]
        if messageType == "attack":
            self.attackToPick = True
            self.attack = int(number)

        elif messageType == "e":
            self.enemyToPick = True
            self.enemy = int(number)



    def mainLoop(self):
        self.goThrougheachTurn(self.combat)


pygame.init()
mainMenu = EncounterStage(1300, 700, "media/MainMenueBackground.png", 12, [Warlock(), Warlock(), Warlock(), Warlock()])
pygame.quit()