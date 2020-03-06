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
        # long init which sets up basic combat elements as well as the GUI itself.
        self.boss = Boss
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
        self.combatBoard = ""


    def redrawAttackBar(self):
        # redraws attack bar, prevents characters from flickering.
        self.combatBoard = pygame.transform.scale(pygame.image.load("Stages/media/combatBoard.png").convert_alpha(),
                                                  (1300, 400))  # loads the combat board.
        self.base.display.blit(self.combatBoard, (0, 300))  # displays the combat board onto the screen.
        pygame.display.update()  # updates screen.

    def drawAttackBarEnemy(self, enemy, attack, player, AOE=False):
        # redraws attack bar with info about enemy attack.
        self.combatBoard = pygame.transform.scale(pygame.image.load("Stages/media/combatBoard.png").convert_alpha(),
                                                  (1300, 400))
        self.base.display.blit(self.combatBoard, (0, 300))

        font = pygame.font.Font(self.font, self.fontsize)
        if AOE:  # if it attacks everyone; AOE means "Area of Effect"
            name = font.render(enemy.name+ " used " + attack.name + " on everyone" , True, self.black)
            pygame.draw.rect(self.base.display, (0, 0, 0), (455, 592, 450, 90))
            pygame.draw.rect(self.base.display, (255, 255, 255), (460, 597, 440, 80))
            self.base.display.blit(name, (490, 608))
        else:  # if it doesn't.
            name = font.render(enemy.name+ " used " + attack.name + " on:" , True, self.black)
            attacke = font.render(player.name, True, self.black)
            pygame.draw.rect(self.base.display, (0, 0, 0), (455, 592, 450, 90))
            pygame.draw.rect(self.base.display, (255, 255, 255), (460, 597, 440, 80))
            self.base.display.blit(name, (490, 608))
            self.base.display.blit(attacke, (490, 628))



        pygame.display.update()

    def drawRoundCount(self, roundCount):
        # puts the current round number to screen.
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
        # If all players are dead, displays to user game over.
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
        # puts the background image on the screen.
        self.base.bgImage = pygame.transform.scale(pygame.image.load(img).convert_alpha(),
                                                   (self.base.screen_height,self.base.screen_width))
        self.base.display.blit(self.base.bgImage, (0, 0))
        if keepBoard:

            self.combatBoard = pygame.transform.scale(pygame.image.load("Stages/media/combatBoard.png").convert_alpha(),
                                                  (1300, 400))

            self.base.display.blit(self.combatBoard, (0, 300))
        pygame.display.update()


    def displayHealth(self, character):
        # displays the health of each character to screen.
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
        # displays all buttons on the screen.
        self.allbuttons = []

        count = 0
        position = {  # position of friendly attacks on the board
            0: [25, 592],
            1: [25, 647],
            2: [230, 592],
            3: [230, 647]
        }
        for attack in character.allAttacks:  # for each attack in all attacks of that character
            button = None
            if attack.onCoolDown:  # if it's on cooldown (can't be used), tells user it can't be used for x turns.
                pygame.draw.rect(self.base.display, (0, 0, 0), (position[count][0], position[count][1], 200, 50))
                pygame.draw.rect(self.base.display, (169,169,169), ( position[count][0] + 5, position[count][1] + 5, 190, 40))
                font = pygame.font.Font(self.font, self.fontsize)

                name = font.render("Cooldown %i Turn(s)" % attack.coolDownTimer, True, self.black)
                self.base.display.blit(name, (position[count][0] + 10, position[count][1] + 15))
            else:  # if not, displays as normal.
                button = StageButton(attack.name, "attack %i %r %s"% (count, attack.isHeal, attack.healType), position[count][0], position[count][1])
                button.height = 50
                button.fontsize = 20



            count += 1
            if button:
                self.allbuttons.append(button)
        self.displayHealth(character)
        count = 0

        position = {  # position of enemy buttons on combat board
            0: [630, 602],
            2: [630, 657],
            1: [835, 602],
            3: [835, 657]
        }

        for enemy in self.combat.turnOrder:  # for each enemy in the turn order

            if enemy.isEnemy:  # if they're an enemy, displays enemy names on the board.
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

        for button in self.allbuttons:  # for each button in all buttons, sets these colours.
            button.defaultColour = (255, 255, 255)
            button.textColor = (0, 0, 0)
            button.hovercolour = self.hoverColour



    def displayCharacter(self):
        # displays all characters to the screen, enemy and friendly.
        positionEnemy = 600
        positionAlly = 520 - (len(self.combat.allies) * 120)

        for character in self.combat.turnOrder:  # for each character in the turn order
            if character.isEnemy:  # if they're enemies puts them on the right hand side of the screen.
                character.CurrentBattlePos = positionEnemy + character.stagePositionX
                self.base.display.blit(
                    pygame.transform.scale(
                        pygame.image.load(character
                                          .imagePath).convert_alpha(), character.scale),
                    (character.CurrentBattlePos, character.stagePositionY)
                )
                self.positionDict[character] = positionEnemy
                self.displayHealth(character)
                positionEnemy += 150
            else:  # if they're friendly puts them on the left hand side of the screen.
                self.base.display.blit(pygame.transform.scale(pygame.image.load(character.imagePath).convert_alpha(),  character.scale), (positionAlly, character.stagePositionY))
                self.positionDict[character] = positionAlly
                self.displayHealth(character)
                positionAlly += 150

        pygame.display.update()

    def listenMouse(self):
        # listens for mouse events.

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

    def goThrougheachTurn(self, combatEncounterInstance, img, boss=False):
        # main combat function; goes through each turn.
        counter = 1
        clicked = False
        death = False

        # while there are still enemies and allies still alive
        while len(combatEncounterInstance.enemies) > 0 and len(combatEncounterInstance.allies) > 0:
            self.drawRoundCount(counter)  # draws the current round counter to screen
            sleep(1)
            self.redrawAttackBar()  # redraws the attack bar to the screen
            for character in combatEncounterInstance.turnOrder:  # for each character still in the combat
                if character.isEnemy:  # if it's an enemy
                    if len(combatEncounterInstance.allies) > 0:  # if there are still allies
                        move = makeMove(character, combatEncounterInstance.allies)  # ENEMY AI: enemy makes a move
                        if move[0].isAOE:  # if it's an attack that attacks everyone
                            self.drawAttackBarEnemy(character, move[0], move[1], True)  # draws the correct info.
                        else:
                            self.drawAttackBarEnemy(character,move[0],move[1])
                        sleep(2)  # gives pause for user
                        death = combatEncounterInstance.calcDamage(move)  # calculates how much damage dealt
                        if death:  # if someone dies
                            self.redraw(img)  # redraws everything so there's one less character
                        self.redrawAttackBar()

                else:  # if it's the player's turn
                    sleep(.3)
                    if len(combatEncounterInstance.enemies) > 0:  # if there's still enemies
                        self.displayButtons(character)  # displays everything again.
                        self.displayHealth(character)
                        while not clicked:  # while the user hasn't done anything
                            for event in pygame.event.get():  # waits for pygame events
                                self.listenMouse()  # and also listens for mouse events.
                                if event.type == pygame.QUIT:  # if the user quits, quits game.
                                    quit()
                                if self.enemyToPick and self.attackToPick:  # if the user has picked something
                                    clicked = True  # button has been clicked.
                        self.selectedAttackButton = None
                        self.selectedEnemyButton = None

                        character.allAttacks[self.attack].startCooldown()  # starts cooldown of attack chosen
                        character.attackSound()  # plays attack sound
                        if self.enemy == "self" or self.enemy == "all":
                            combatEncounterInstance.calcDamage([character.allAttacks[self.attack], self.enemy],
                                                               character)
                        else:
                            death = combatEncounterInstance.calcDamage(
                                [character.allAttacks[self.attack],
                                 combatEncounterInstance.turnOrder[self.enemy]],
                                character,
                                boss)
                        if death:
                            self.redraw(img)
                        clicked = False
                        self.attackToPick = False
                        self.enemyToPick = False
                    else:
                        break
                if death:
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
        # redraws characters and background.
        self.drawBackground(img)
        self.displayCharacter()
        pygame.display.update()

    def mouseClick(self, button):
        # detects mouse click
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
        # begins the whole program for the encounter.
        self.goThrougheachTurn(self.combat, img, self.boss)


if __name__ == "__main__":
    # manual testing purposes.
    baseScreen = BaseStage(1300, 700)
    pygame.init()
    pygame.mixer.init()
    EncounterStage(baseScreen, "Stages/media/MainMenueBackground2.png", 7, [Fighter(), Warlock(),Fighter()])
    pygame.quit()
