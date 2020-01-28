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

    def takeDamage(self, amount):
        self.health -= amount


    def setHealth(self, newHealth):
        self.health = newHealth + calc_attribute_bonus(self.constitution)

    def rollInitative(self):
        return randint + calc_attribute_bonus(self.dexterity)

    def increaseStr(self, amount):
        self.strength += amount

    def increaseDex(self, amount):
        self.strength += amount

    def increaseConst(self, amount):
        self.strength += amount

    def increaseInt(self, amount):
        self.strength += amount

    def increaseAC(self, amount):
        self.strength += amount

    def decreaseStr(self, amount):
        self.strength -= amount

    def decreaseDex(self, amount):
        self.strength -= amount

    def decreaseConst(self, amount):
        self.strength -= amount

    def decreaseInt(self, amount):
        self.strength -= amount

    def decreaseAC(self, amount):
        self.strength -= amount

    def levelUp(self, chosenAttribute):
        atributeDict = {
            "str": self.increaseStr,
            "dex": self.increaseDex,
            "con": self.increaseConst,
            "int": self.increaseInt,
            "ac": self.increaseAC
        }
        atributeDict[chosenAttribute](1)
