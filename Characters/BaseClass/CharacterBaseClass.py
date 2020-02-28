from random import randint, choice as RChoice
import pygame
from Characters.sharedFunctions import calc_attribute_bonus
from time import sleep


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

    def increaseAC(self, amount):
        self.ArmorClass += amount

    def levelUp(self, chosenAttribute):
        attributeDict = {
            "str": self.increaseStr,
            "dex": self.increaseDex,
            "con": self.increaseConst,
            "int": self.increaseInt,
            "ac": self.increaseAC
        }
        attributeDict[chosenAttribute](1)

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
