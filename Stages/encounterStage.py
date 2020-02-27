import pygame, sys, os
from pygame.locals import *
from Stages.baseStageClass import BaseStage

from Characters.playerClasses.warlock import Warlock
from CombatSystem.enemyMove import makeMove
from Stages.baseStageClass import *
from CombatSystem.combat import *


class EncounterStage():
    def __init__(self, screen, levelImage, crLevel, listOfPlayers):
        self.defaultColour = (120, 120, 120)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.positionDict = {}
        self.characterDict = {}
        self.font = 'Stages/media/Chapaza.ttf'
        self.fontsize = 20
        self.enemy = None
        self.enemyToPick = False
        self.attack = None
        self.attackToPick = False
        self.selectedEnemyButton = None
        self.selectedAttackButton = None
        self.hoverColour = (255, 184, 148)
        self.base = screen
        self.selectColour = (152, 204, 148)
        self.drawBackground(levelImage)
        self.combat = combatEncounter()
        self.combat.setUp(crLevel, listOfPlayers)
        self.turnOrder = self.combat.turnOrder
        self.displayCharacter()
        self.mainLoop(levelImage)
        self.enemies = []

    def drawBackground(self, img):
        self.base.bgImage = pygame.transform.scale(pygame.image.load(img).convert(),
                                                   (self.base.screen_height,self.base.screen_width))
        pygame.display.update()

        self.combatBoard = pygame.transform.scale(pygame.image.load("Stages/media/combatBoard.png").convert_alpha(),
                                                  (1300, 400))

        self.displayBattle()

    def displayBattle(self):
        self.base.display.blit(self.base.bgImage, (0, 0))
        self.base.display.blit(self.combatBoard, (0, 300))
        pygame.display.update()


    def displayHealth(self, character, position=None):



        percentHealth = character.health / character.maxHealth
        health = str(character.health) + "/" + str(character.maxHealth)
        font = pygame.font.Font(self.font, self.fontsize)
        name = font.render(character.name, True, self.black)
        text = font.render(health, True, self.black)



        pygame.draw.rect(self.base.display, (0, 0, 0), (455, 592, 150, 50))
        pygame.draw.rect(self.base.display, (255, 255, 255), (460, 597, 140, 40))
        pygame.display.set_caption("Traylian")
        self.base.display.blit(name, (490, 608))

        percentHealthDisplay = int(180 * (percentHealth))
        pygame.draw.rect(self.base.display, (0, 0, 0), (435, 647, 190, 50))
        pygame.draw.rect(self.base.display, (255, 255, 255), (440, 652, 180, 40))
        pygame.draw.rect(self.base.display, (138, 7, 7), (440, 652, percentHealthDisplay, 40))
        self.base.display.blit(text, (490, 663))


    def displayButtons(self, character):
        self.allbuttons = []

        count = 0
        position = {
            0: [25, 592],
            1: [25, 647],
            2: [230, 592],
            3: [230, 647]
        }
        for attack in character.allAttacks:

            button = StageButton(attack.name, "attack %i"% count, position[count][0], position[count][1])
            button.height = 50
            button.fontsize = 20

            count += 1
            self.allbuttons.append(button)
        self.displayHealth(character)
        count = 0

        position = {
            0: [625, 592],
            2: [625, 647],
            1: [830, 592],
            3: [830, 647]
        }

        for enemy in self.combat.enemies:
            button = StageButton("Enemy %i" % enemy.combatPos, "e %i" % count, position[count][0], position[count][1])
            button.height = 40
            button.fontsize = 20

            self.allbuttons.append(button)

            percentHealth = enemy.health / enemy.maxHealth
            percentHealthDisplay = int(198 * (percentHealth))

            pygame.draw.rect(self.base.display, (0, 0, 0), (position[count][0], position[count][1] - 10, 200, 10))
            pygame.draw.rect(self.base.display, (255, 255, 255), (position[count][0]+1, position[count][1] -9, 198, 9))

            pygame.draw.rect(self.base.display, (138, 7, 7),
                                  (position[count][0]+1, position[count][1]- 9, percentHealthDisplay, 9))

            count += 1

        for button in self.allbuttons:
            button.defaultColour = (255, 255, 255)
            button.textColor = (0, 0, 0)
            button.hovercolour = self.hoverColour



    def displayCharacter(self):
        positionEnemy = 600
        positionAlly = 370
        for character in self.combat.allCharsInFight:
            if character.isEnemy:
                character.CurrentBattlePos = positionEnemy + character.stagePositionX
                self.base.display.blit(
                    pygame.transform.scale(
                        pygame.image.load(character.imagePath).convert_alpha(), character.scale),
                    (character.CurrentBattlePos, character.stagePositionY)
                )
                self.positionDict[character] = positionEnemy
                self.displayHealth(character, self.positionDict[character])
                positionEnemy += 150
            else:
                self.base.display.blit(pygame.transform.scale(pygame.image.load(character.imagePath).convert_alpha(), (330, 330)), (positionAlly, 250))
                self.positionDict[character] = positionAlly
                self.displayHealth(character, self.positionDict[character])
                positionAlly -= 150
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

    def goThrougheachTurn(self, combatEncounterInstance, img):
        count = 0
        clicked = False
        while len(combatEncounterInstance.enemies) > 0 and len(combatEncounterInstance.allies) > 0:
            for character in combatEncounterInstance.turnOrder:
                if character.isEnemy:
                    move = makeMove(character, combatEncounterInstance.allies)
                    death = combatEncounterInstance.calcDamage(move)

                else:
                    if len(combatEncounterInstance.enemies) > 0:
                        self.displayButtons(character)
                        self.displayHealth(character)
                        while not clicked:

                            for event in pygame.event.get():
                                self.listenMouse()
                                if event.type == pygame.QUIT:
                                    quit()
                                if self.enemyToPick == True and self.attackToPick == True:
                                    clicked = True
                        self.selectedAttackButton = None
                        self.selectedEnemyButton = None
                        character.allAttacks[self.attack].startCooldown()
                        character.attackSound()
                        death = combatEncounterInstance.calcDamage([character.allAttacks[self.attack].calcDamage(), combatEncounterInstance.enemies[self.enemy]], character)

                        if death == True:
                            self.redraw(img)
                        if len(combatEncounterInstance.enemies) > 0:
                            self.displayHealth(combatEncounterInstance.enemies[self.enemy], self.positionDict[combatEncounterInstance.enemies[self.enemy]])


                        clicked = False
                        self.attackToPick = False
                        self.enemyToPick = False
                    else:
                        break
                for attack in character.allAttacks:
                    attack.reduceCoolDown()
            count += 1

        if len(combatEncounterInstance.enemies) <= 0:
            print("Allys won\n\n")
        else:
            print("Enemys won\n\n")



    def redraw(self, img):
        self.drawBackground(img)
        self.displayCharacter()
        pygame.display.update()

    def mouseClick(self, button):
        messageType, number = button.exitMessage.split()[0], button.exitMessage.split()[1]
        if messageType == "attack":
            if self.selectedAttackButton != None:
                self.selectedAttackButton.defaultColour = self.white
            button.defaultColour = self.selectColour
            self.attackToPick = True
            self.attack = int(number)
            self.selectedAttackButton = button

        elif messageType == "e":
            if self.selectedEnemyButton != None:
                self.selectedEnemyButton.defaultColour = self.white
            button.defaultColour = self.selectColour
            self.enemyToPick = True
            self.enemy = int(number)
            self.selectedEnemyButton = button

    def mainLoop(self, img):
        self.goThrougheachTurn(self.combat, img)


if __name__ == "__main__":
    baseScreen = BaseStage(1300, 700)
    pygame.init()
    pygame.mixer.init()
    EncounterStage(baseScreen, "Stages/media/MainMenueBackground2.png", 4, [Warlock(), Warlock()])
    pygame.quit()
