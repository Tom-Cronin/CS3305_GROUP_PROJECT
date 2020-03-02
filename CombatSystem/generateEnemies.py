from CombatSystem.MonsterDictionary import CR_MAX_VALUE as CR_Max,CR_MIN_VALUE as CR_Min, dictionaryOfMonsters as DM, dictionaryOfBoss as DB
from random import randint


dictionaryOfMonsters = DM
dictionaryOfBoss = DB
CR_MAX_VALUE = CR_Max
CR_MIN_VALUE = CR_Min

def createEnemyInstances(enemyCROrder, Boss=False):
    if Boss:
        boss = dictionaryOfBoss.get(1)[0]()
        return [boss]
    enemies = []
    count = 1
    for enemyCR in enemyCROrder:
        possibleEnemysOfCR = dictionaryOfMonsters.get(enemyCR)
        enemy = possibleEnemysOfCR[randint(0, len(possibleEnemysOfCR) - 1)]()
        enemy.combatPos = count
        count += 1
        enemies.append(enemy)
    return enemies


def minCRValue(crTotal, enemySpacesRemaining):
    minCRVal = CR_MIN_VALUE
    while enemySpacesRemaining * minCRVal < crTotal <= enemySpacesRemaining * CR_MAX_VALUE:
        minCRVal += 1
    return minCRVal


# only works with CR's less than the max CR * 4
def generateEnemies(totalChalenegeLevel, Boss=False):
    spaces = 4
    if Boss:
        return createEnemyInstances([1], Boss)
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

