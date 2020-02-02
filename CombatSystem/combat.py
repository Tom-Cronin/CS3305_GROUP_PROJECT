from CombatSystem.generateEnemies import generateEnemies
# only  uses while making will be removed
from Characters.playerClasses.warlock import Warlock

enemies = []
allies = []
turnOrder = []

def calcDamage(charTakingDamage, Damage)
    charTakingDamage = Warlock()
    charTakingDamage.takeDamage(Damage)


def goThrougheachTurn():
    global turnOrder, allies, enemies
    while len(enemies) > 0 and len(allies) > 0:
        for character in turnOrder:
            if character.isEnemy:
                pass
                # call enemy combat system
                #calc damage
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
    # TODO get call to turn order
    turnOrder = allies + enemies

print(enemies)
setUp(4, [Warlock(), Warlock(), Warlock(), Warlock()])
goThrougheachTurn()

