from CombatSystem.generateEnemies import generateEnemies
from CombatSystem.turnOrder import turnOrder as getTurnOrder
# only  uses while making will be removed
from Characters.playerClasses.warlock import Warlock

enemies = []
allies = []
turnOrder = []

def calcDamage(charTakingDamage, Damage):
    global enemies, turnOrder, allies
    charTakingDamage = Warlock()
    charTakingDamage.takeDamage(Damage)
    if charTakingDamage.health <= 0:
        if charTakingDamage.isEnemy:
            enemies.remove(charTakingDamage)
        else:
            allies.remove(charTakingDamage)
        turnOrder.remove(charTakingDamage)
        del charTakingDamage



def goThrougheachTurn():
    global turnOrder, allies, enemies
    while len(enemies) > 0 and len(allies) > 0:
        for character in turnOrder:
            if character.isEnemy:
                pass
                # call enemy combat system
                # calc damage
                # if char health less than 0 del that char
            else:
                # call player
                # calc damage
                # if char health is less than 0 del that char
                pass


def setUp(crChalengeLevel, listOfPlayers):
    global enemies, allies, turnOrder
    enemies = generateEnemies(crChalengeLevel)
    allies = listOfPlayers
    turnOrder = allies + enemies
    turnOrder = getTurnOrder(turnOrder)


setUp(4, [Warlock(), Warlock(), Warlock(), Warlock()])


