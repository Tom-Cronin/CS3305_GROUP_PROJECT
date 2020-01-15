import random


class Character:
    def __init__(self):
        self.health = 0

        self.constitution = 0 # health
        self.dexterity = 0 # ranged / dagger damage
        self.strength = 0 # melee damage
        self.inteligence = 0 # spellcasting? if implemented
        self.initiative = 0 # Turn order
        self.ArmorClass = 0 # gives chance to block an attack

    def setAC(self, AC):
        self.ArmorClass = AC

    def getAC(self):
        return self.ArmorClass

    def setHealth(self, newHealth):
        self.health = newHealth + self.constitution

    def getHealth(self):
        return self.health

    def setConstitution(self, newConstitution):
        self.constitution = newConstitution

    def getConstitution(self):
        return self.constitution

    def setDex(self, newDex):
        self.dexterity = newDex

    def getDex(self):
        return self.dexterity

    def setStrength(self, newStrength):
        self.strength = newStrength

    def getStrenght(self):
        return self.strength

    def setInt(self, newInt):
        self.inteligence = newInt

    def getInt(self):
        return self.inteligence

    def setInitiative(self, newInitiative):
        self.initiative = newInitiative

    def getInitative(self):
        return self.initiative

    def rollInitative(self):
        roll = random.random * 19
        roll + 1
        roll += self.getInitative()
        return roll


