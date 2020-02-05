from CombatSystem.generateEnemies import generateEnemies
from CombatSystem.turnOrder import turnOrder as getTurnOrder
from CombatSystem.enemyMove import makeMove
# only  uses while making will be removed
from Characters.playerClasses.warlock import Warlock

enemies = []
allies = []
turnOrder = []

def calcDamage(tupleOfdamgeAndChar):
    Damage = tupleOfdamgeAndChar[0]
    charTakingDamage = tupleOfdamgeAndChar[1]
    global enemies, turnOrder, allies
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
                # call enemy combat system
                # calc damage
                # if char health less than 0 del that char
                calcDamage(makeMove(character, allies))

            else:
                # call player
                # calc damage
                # if char health is less than 0 del that char
                calcDamage(makeMove(character, enemies))
    if len(enemies) <= 0:
        print("Allys won")
    else:
        print("Enemys won")


def setUp(crChalengeLevel, listOfPlayers):
    global enemies, allies, turnOrder
    enemies = generateEnemies(crChalengeLevel)
    allies = listOfPlayers
    #allies = generateEnemies(crChalengeLevel)
    #for ally in allies:
    #    ally.isEnemy = False
    turnOrder = allies + enemies
    turnOrder = getTurnOrder(turnOrder)
    goThrougheachTurn()

if __name__ == "__main__":
    setUp(99, [Warlock(), Warlock(), Warlock(), Warlock()])


