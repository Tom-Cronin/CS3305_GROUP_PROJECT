from CombatSystem.generateEnemies import generateEnemies
from CombatSystem.turnOrder import turnOrder as getTurnOrder
from CombatSystem.enemyMove import makeMove
# only  uses while making will be removed
from Characters.playerClasses.warlock import Warlock

enemies = []
allies = []
turnOrder = []
allCharsInFight = []

def calcDamage(tupleOfdamgeAndChar, char=None):
    Damage = tupleOfdamgeAndChar[0]
    charTakingDamage = tupleOfdamgeAndChar[1]
    global enemies, turnOrder, allies
    charTakingDamage.takeDamage(Damage)
    if charTakingDamage.health <= 0:
        print("Rest in peace: ", charTakingDamage)
        if charTakingDamage.isEnemy:
            enemies.remove(charTakingDamage)
            char.killCounter()
        else:
            allies.remove(charTakingDamage)
        turnOrder.remove(charTakingDamage)
        del charTakingDamage



def goThrougheachTurn():
    global turnOrder, allies, enemies, allCharsInFight
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
                calcDamage(makeMove(character, enemies), character)
    if len(enemies) <= 0:
        print("Allys won\n\n")
    else:
        print("Enemys won\n\n")
    for char in allCharsInFight:
        print(char)



def setUp(crChalengeLevel, listOfPlayers):
    global enemies, allies, turnOrder, allCharsInFight
    enemies = generateEnemies(crChalengeLevel)
    print(enemies)
    allies = listOfPlayers
    #allies = generateEnemies(crChalengeLevel)
    #for ally in allies:
    #    ally.isEnemy = False
    turnOrder = allies + enemies
    allCharsInFight = turnOrder
    turnOrder = getTurnOrder(turnOrder)
    goThrougheachTurn()

if __name__ == "__main__":
    setUp(6, [Warlock(), Warlock(), Warlock(), Warlock()])


