import pygame, sys, os
from pygame.locals import *
from Stages.baseStageClass import BaseStage
from time import sleep

from Characters.playerClasses.warlock import Warlock
from Characters.playerClasses.fighter import Fighter
from CombatSystem.enemyMove import makeMove
from Stages.baseStageClass import *
from CombatSystem.combat import *


class EncounterStage():
    def __init__(self, screen, levelImage, crLevel, listOfPlayers, Boss=False):
        print(Boss)
        self.levelImage = levelImage
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
        self.combat.setUp(crLevel, listOfPlayers, Boss)
        self.turnOrder = self.combat.turnOrder
        self.displayCharacter()
        self.mainLoop(levelImage)
        self.enemies = []
        self.combatBoard=""


    def redrawAttackBar(self):
        self.combatBoard = pygame.transform.scale(pygame.image.load("Stages/media/combatBoard.png").convert_alpha(),
                                                  (1300, 400))
        self.base.display.blit(self.combatBoard, (0, 300))
        pygame.display.update()

    def drawAttackBarEnemy(self, enemy, attack, player):
        self.combatBoard = pygame.transform.scale(pygame.image.load("Stages/media/combatBoard.png").convert_alpha(),
                                                  (1300, 400))
        self.base.display.blit(self.combatBoard, (0, 300))

        font = pygame.font.Font(self.font, self.fontsize)
        name = font.render(enemy.name+ " used " + attack.name + " on " + player.name, True, self.black)


        pygame.draw.rect(self.base.display, (0, 0, 0), (455, 592, 450, 50))
        pygame.draw.rect(self.base.display, (255, 255, 255), (460, 597, 440, 40))
        self.base.display.blit(name, (490, 608))

        pygame.display.update()

    def drawRoundCount(self, roundCount):
            self.combatBoard = pygame.transform.scale(pygame.image.load("Stages/media/combatBoard.png").convert_alpha(),
                                                      (1300, 400))
            self.base.display.blit(self.combatBoard, (0, 300))

            font = pygame.font.Font(self.font, self.fontsize)
            name = font.render("Round "+ str(roundCount), True, self.black)

            pygame.draw.rect(self.base.display, (0, 0, 0), (455, 592, 250, 50))
            pygame.draw.rect(self.base.display, (255, 255, 255), (460, 597, 240, 40))
            self.base.display.blit(name, (490, 608))

            pygame.display.update()

    def playersDead(self):
            self.combatBoard = pygame.transform.scale(pygame.image.load("Stages/media/combatBoard.png").convert_alpha(),
                                                      (1300, 400))
            self.base.display.blit(self.combatBoard, (0, 300))

            font = pygame.font.Font(self.font, self.fontsize)
            name = font.render("Game Over", True, self.black)

            pygame.draw.rect(self.base.display, (0, 0, 0), (455, 592, 250, 50))
            pygame.draw.rect(self.base.display, (255, 255, 255), (460, 597, 240, 40))
            self.base.display.blit(name, (490, 608))

            pygame.display.update()
    def drawBackground(self, img, keepBoard=True):
        self.base.bgImage = pygame.transform.scale(pygame.image.load(img).convert_alpha(),
                                                   (self.base.screen_height,self.base.screen_width))
        self.base.display.blit(self.base.bgImage, (0, 0))
        if keepBoard:
            print("youch")

            self.combatBoard = pygame.transform.scale(pygame.image.load("Stages/media/combatBoard.png").convert_alpha(),
                                                  (1300, 400))

            self.base.display.blit(self.combatBoard, (0, 300))
        pygame.display.update()


    def displayHealth(self, character):



        percentHealth = character.health / character.maxHealth
        health = str(character.health) + "/" + str(character.maxHealth)
        font = pygame.font.Font(self.font, self.fontsize)
        name = font.render(character.name, True, self.black)
        text = font.render(health, True, self.black)



        pygame.draw.rect(self.base.display, (0, 0, 0), (445, 592, 170, 50))
        pygame.draw.rect(self.base.display, (255, 255, 255), (450, 597, 160, 40))
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
            button = None
            if attack.onCoolDown:
                pygame.draw.rect(self.base.display, (0, 0, 0), (position[count][0], position[count][1], 200, 50))
                pygame.draw.rect(self.base.display, (169,169,169), ( position[count][0] + 5, position[count][1] + 5, 190, 40))
                font = pygame.font.Font(self.font, self.fontsize)

                name = font.render("Cooldown %i Turn(s)" % attack.coolDownTimer, True, self.black)
                self.base.display.blit(name, (position[count][0] + 10, position[count][1] + 15))
            else:
                button = StageButton(attack.name, "attack %i %r %s"% (count, attack.isHeal, attack.healType), position[count][0], position[count][1])
                button.height = 50
                button.fontsize = 20



            count += 1
            if button:
                self.allbuttons.append(button)
        self.displayHealth(character)
        count = 0

        position = {
            0: [630, 602],
            2: [630, 657],
            1: [835, 602],
            3: [835, 657]
        }

        for enemy in self.combat.turnOrder:

            if enemy.isEnemy:
                button = StageButton(enemy.name , "e %i NA NA" % enemy.TurnOrderPosOfEnemys, position[count][0], position[count][1])
                button.height = 40
                button.fontsize = 20

                self.allbuttons.append(button)

                percentHealth = enemy.health / enemy.maxHealth
                percentHealthDisplay = int(198 * (percentHealth))

                pygame.draw.rect(self.base.display, (0, 0, 0), (position[count][0], position[count][1] - 10, 200, 10))
                pygame.draw.rect(self.base.display, (255, 255, 255), (position[count][0]+1, position[count][1] -9, 198, 9))

                pygame.draw.rect(self.base.display, (138, 7, 7),
                                      (position[count][0]+1, position[count][1]- 9, percentHealthDisplay, 9))
                pygame.display.update()

                count += 1

        for button in self.allbuttons:
            button.defaultColour = (255, 255, 255)
            button.textColor = (0, 0, 0)
            button.hovercolour = self.hoverColour



    def displayCharacter(self):
        positionEnemy = 600

        # positionAlly = -80
        positionAlly = 520 - (len(self.combat.allies) * 150)
        for character in self.combat.turnOrder:
            if character.isEnemy:
                character.CurrentBattlePos = positionEnemy + character.stagePositionX
                self.base.display.blit(
                    pygame.transform.scale(
                        pygame.image.load(character.imagePath).convert_alpha(), character.scale),
                    (character.CurrentBattlePos, character.stagePositionY)
                )
                self.positionDict[character] = positionEnemy
                self.displayHealth(character)
                positionEnemy += 150
            else:
                self.base.display.blit(pygame.transform.scale(pygame.image.load(character.imagePath).convert_alpha(),  character.scale), (positionAlly, 250))
                self.positionDict[character] = positionAlly
                self.displayHealth(character)
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

    def goThrougheachTurn(self, combatEncounterInstance, img):
        counter = 1
        clicked = False
        death = False

        while len(combatEncounterInstance.enemies) > 0 and len(combatEncounterInstance.allies) > 0:
            self.drawRoundCount(counter)
            sleep(1)
            self.redrawAttackBar()
            for character in combatEncounterInstance.turnOrder:

                if character.isEnemy :
                    if len(combatEncounterInstance.allies) > 0:
                        move = makeMove(character, combatEncounterInstance.allies)
                        self.drawAttackBarEnemy(character,move[0],move[1])
                        sleep(2)
                        death = combatEncounterInstance.calcDamage(move)
                        if death == True:
                            self.redraw(img)
                        self.redrawAttackBar()

                else:
                    sleep(.3)
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
                        if self.enemy == "self" or self.enemy == "all":
                            combatEncounterInstance.calcDamage([character.allAttacks[self.attack], self.enemy],
                                                               character)
                        else:
                            death = combatEncounterInstance.calcDamage([character.allAttacks[self.attack], combatEncounterInstance.turnOrder[self.enemy]], character)

                        if death == True:
                            self.redraw(img)

                        clicked = False
                        self.attackToPick = False
                        self.enemyToPick = False
                    else:
                        break
                if death == True:
                    for char in combatEncounterInstance.turnOrder:
                        char.TurnOrderPosOfEnemys = self.turnOrder.index(char)
                for attack in character.allAttacks:
                    attack.reduceCoolDown()
            counter += 1

        if len(combatEncounterInstance.enemies) <= 0:
            sleep(1)
            for ally in self.combat.allies:
                for attack in ally.allAttacks:
                    attack.resetCoolDown()
            self.drawBackground(self.levelImage, False)
        else:
            sleep(.5)
            self.playersDead()
            sleep(1)







    def redraw(self, img):
        self.drawBackground(img)
        self.displayCharacter()
        pygame.display.update()

    def mouseClick(self, button):
        messageType, number, heal, type = button.exitMessage.split()[0], \
                                          button.exitMessage.split()[1], \
                                          button.exitMessage.split()[2], \
                                          button.exitMessage.split()[3]
        if messageType == "attack":
            if heal == "True":
                self.enemyToPick = True
                self.enemy = type
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
    EncounterStage(baseScreen, "Stages/media/MainMenueBackground2.png", 7, [Fighter(), Warlock(),Fighter()])
    pygame.quit()
