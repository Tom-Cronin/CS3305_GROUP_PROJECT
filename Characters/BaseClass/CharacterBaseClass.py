from random import randint, choice as RChoice
import pygame
from Characters.sharedFunctions import calc_attribute_bonus
from time import sleep
from Characters.attacks.baseAttackClass import BaseAttack


class Character:
    def __init__(self):
        self.maxHealth = 0
        self.health = self.maxHealth
        self.name = self.generateName()

        self.constitution = 0 # health
        self.dexterity = 0 # ranged / dagger damage
        self.strength = 0 # melee damage
        self.intelligence = 0 # intelligence? if implemented
        self.ArmorClass = 0 # gives chance to block an attack
        self.isEnemy = True
        self.totalKills = 0

        self.imagePath = None

        self.combatPos = 0

        self.attackSoundPath = "blank"
        self.scale = (0,0)
        self.stagePositionY = 250
        self.stagePositionX = 0

        self.CurrentBattlePos = 0
        self.TurnOrderPosOfEnemys = 0

        self.attack_slot_1 = BaseAttack()
        self.attack_slot_2 = BaseAttack()
        self.attack_slot_3 = BaseAttack()
        self.attack_slot_4 = BaseAttack()

        self.attackBonus = []
        self.nonInitAttacks= []

        self.allAttacks = [self.attack_slot_1, self.attack_slot_2, self.attack_slot_3, self.attack_slot_4]

    def killCounter(self):
        self.totalKills += 1

    def takeDamage(self, amount):
        self.health -= amount


    def setHealth(self, newHealth):
        self.maxHealth = newHealth + calc_attribute_bonus(self.constitution)
        self.health = self.maxHealth

    def rollInitative(self):
        return randint(0, 20) + calc_attribute_bonus(self.dexterity)

    def increaseStr(self, amount):
        self.strength += amount

    def increaseDex(self, amount):
        self.dexterity += amount

    def increaseConst(self, amount):
        self.constitution += amount

    def increaseInt(self, amount):
        self.intelligence += amount

    def charFullLevelUp(self, stattAmmoun=10):
        listOfAllAtts = ["strength", "dexterity", "constitution", "intelligence"]
        for att in listOfAllAtts:
            self.levelUp(att, stattAmmoun)

    def updateBonusList(self):
        self.attackBonus = []

    def levelUp(self, chosenAttribute, ammount):
        attributeDict = {
            "strength": self.increaseStr,
            "dexterity": self.increaseDex,
            "constitution": self.increaseConst,
            "intelligence": self.increaseInt
        }
        attributeDict[chosenAttribute](ammount)
        self.updateBonusList()

        self.selfUpdate()

    def selfUpdate(self):
        count = 0
        for bonus in self.attackBonus:
            if count == 0:
                self.attack_slot_1 =self.nonInitAttacks[count](bonus)
            elif count == 1:
                self.attack_slot_2 = self.nonInitAttacks[count](bonus)
            elif count == 2:
                self.attack_slot_3 = self.nonInitAttacks[count](bonus)
            elif count == 3:
                self.attack_slot_4 = self.nonInitAttacks[count](bonus)
            count +=1
        self.allAttacks = [self.attack_slot_1, self.attack_slot_2, self.attack_slot_3, self.attack_slot_4]

    def attackSound(self):
        # if self.attackSoundPath != "blank":
        #     pygame.mixer.init()
        #     attackSound = pygame.mixer.Sound(self.attackSoundPath)
        #     attackSound.set_volume(0.025)
        #     attackSound.play()
        #     sleep(attackSound.get_length())
        pass

    def heal(self, ammount):
        self.health += ammount
        if self.health > self.maxHealth:
            self.health = self.maxHealth

    def generateName(self):
        return RChoice(open('Characters/BaseClass/nameLists.txt').read().splitlines())

