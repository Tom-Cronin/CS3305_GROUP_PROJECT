from Characters.BaseClass.CharacterBaseClass import Character
from Characters.enemyClasses.GateGuard import GateGuard
from Characters.enemyClasses.Hag import Hag
from Characters.enemyClasses.Rat import Rat
from Characters.enemyClasses.ShadowJest import ShadowJest
from Characters.enemyClasses.Shadowling import Shadowling
from random import randint

# TODO CR(?) based encounters, to balance out game.


class Encounter:
    def __init__(self):
        self.listOfEnemies = [Hag(), Rat(), GateGuard(), ShadowJest(), Shadowling()]
        self.playerCharacters = [Character(), Character(), Character(), Character()]
        self.turnOrder = self.turnOrder()

    def turnOrder(self):
        turnOrderStack = []
        thidict = {}
        enemy1 = self.listOfEnemies[randint(0, 4)]
        enemy2 = self.listOfEnemies[randint(0, 4)]
        enemy3 = self.listOfEnemies[randint(0, 4)]
        enemy4 = self.listOfEnemies[randint(0, 4)]
        thidict[enemy1] = enemy1.rollInitative()
        thidict[enemy2] = enemy2.rollInitative()
        thidict[enemy3] = enemy3.rollInitative()
        thidict[enemy4] = enemy4.rollInitative()
        thidict[self.playerCharacters[0]] = self.playerCharacters[0].rollInitative()
        thidict[self.playerCharacters[1]] = self.playerCharacters[1].rollInitative()
        thidict[self.playerCharacters[2]] = self.playerCharacters[2].rollInitative()
        thidict[self.playerCharacters[3]] = self.playerCharacters[3].rollInitative()

        sortDict = {k: v for k, v in sorted(thidict.items(), reverse=True, key=lambda item: item[1])}
        for character in sortDict:
            turnOrderStack.append(character)
        return turnOrderStack

    def determineTurn(self):
        for character in self.turnOrder:
            if character in self.listOfEnemies:



instance = Encounter()