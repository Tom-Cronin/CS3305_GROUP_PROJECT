from Characters.enemyClasses import Hag, Rat, ShadowJest, Shadowling
from random import randint
# currently highest cr implemented monster is CR 3
# lowest ranking is cr 1
CR_MAX_VALUE = 3
CR_MIN_VALUE = 1

dictionaryOfMonsters = {
    1: [Shadowling.Shadowling, Rat.Rat],
    2: [ShadowJest.ShadowJest],
    3: [Hag.Hag]
}

def createEnemyInstances(enemyCROrder):
    enemies = []
    for enemyCR in enemyCROrder:
        possibleEnemysOfCR = dictionaryOfMonsters.get(enemyCR)
        enemies.append(possibleEnemysOfCR[randint(0, len(possibleEnemysOfCR) - 1)]())
    return enemies

def minCRValue(crTotal, spaces):
    minVal = CR_MIN_VALUE
    while spaces * minVal < crTotal <= spaces * CR_MAX_VALUE:
        minVal += 1
    return minVal

# only works with CR's less than the max CR
def generateEnemies(totalChalenegeLevel):
    spaces = 4
    enemyCROrder = []
    while totalChalenegeLevel > 0:
        min = minCRValue(totalChalenegeLevel, spaces)
        if totalChalenegeLevel >= CR_MAX_VALUE:
            randomEnemyCR = randint(min, CR_MAX_VALUE)
        else:
            randomEnemyCR = randint(min, totalChalenegeLevel)
        enemyCROrder.append(randomEnemyCR)
        totalChalenegeLevel -= randomEnemyCR
        spaces -= 1
    return createEnemyInstances(enemyCROrder)

