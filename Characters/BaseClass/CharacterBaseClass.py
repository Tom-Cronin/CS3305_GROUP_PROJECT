from random import randint

from Characters.sharedFunctions import calc_attribute_bonus


class Character:
    def __init__(self):
        self.health = 0

        self.constitution = 0 # health
        self.dexterity = 0 # ranged / dagger damage
        self.strength = 0 # melee damage
        self.intelligence = 0 # intelligence? if implemented
        self.ArmorClass = 0 # gives chance to block an attack
        self.isEnemy = True
        self.totalKills = 0

    def killCounter(self):
        self.totalKills += 1

    def takeDamage(self, amount):
        self.health -= amount


    def setHealth(self, newHealth):
        self.health = newHealth + calc_attribute_bonus(self.constitution)

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

    def decreaseStr(self, amount):
        self.strength -= amount

    def decreaseDex(self, amount):
        self.dexterity -= amount

    def decreaseConst(self, amount):
        self.constitution -= amount

    def decreaseInt(self, amount):
        self.intelligence -= amount

    def decreaseAC(self, amount):
        self.ArmorClass -= amount

    def levelUp(self, chosenAttribute):
        attributeDict = {
            "str": self.increaseStr,
            "dex": self.increaseDex,
            "con": self.increaseConst,
            "int": self.increaseInt,
            "ac": self.increaseAC
        }
        attributeDict[chosenAttribute](1)
