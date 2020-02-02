from Characters.enemyClasses.ShadowJest import ShadowJest
from Characters.BaseClass.CharacterBaseClass import Character


def turnOrder(combatList):
    turnOrderStack = []
    thidict = {}

    for charcater in combatList:
        rollinit = charcater.rollInitative()
        thidict[charcater] = rollinit
    sortDict = {k: v for k, v in sorted(thidict.items(), reverse=True, key=lambda item: item[1] )}
    for character in sortDict:
        turnOrderStack.append(character)
    return turnOrderStack












