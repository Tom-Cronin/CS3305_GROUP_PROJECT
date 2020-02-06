from CombatSystem.generateEnemies import generateEnemies
from CombatSystem.turnOrder import turnOrder as getTurnOrder
from CombatSystem.enemyMove import makeMove
# only  uses while making will be removed
from Characters.playerClasses.warlock import Warlock
class combatEncounter(object):
    def __init__(self):
        self.enemies = []
        self.allies = []
        self.turnOrder = []
        self.allCharsInFight = []

    def calcDamage(self, tupleOfdamgeAndChar, char=None):
        Damage = tupleOfdamgeAndChar[0]
        charTakingDamage = tupleOfdamgeAndChar[1]
        global enemies, turnOrder, allies
        charTakingDamage.takeDamage(Damage)
        if charTakingDamage.health <= 0:
            if charTakingDamage.isEnemy:
                self.enemies.remove(charTakingDamage)
                char.killCounter()
            else:
                self.allies.remove(charTakingDamage)
            self.turnOrder.remove(charTakingDamage)
            del charTakingDamage



    def goThrougheachTurn(self):
        count = 0
        while len(self.enemies) > 0 and len(self.allies) > 0:
            for character in self.turnOrder:
                if character.isEnemy:
                    self.calcDamage(makeMove(character, self.allies))

                else:
                    self.calcDamage(makeMove(character, self.enemies), character)
                for attack in character.allAttacks:
                    attack.reduceCoolDown()
            count += 1

        if len(self.enemies) <= 0:
            print("Allys won\n\n")
        else:
            print("Enemys won\n\n")
        print(count)
        # for char in allCharsInFight:
        #     print(char)



    def setUp(self, crChalengeLevel, listOfPlayers):
        self.enemies = generateEnemies(crChalengeLevel)
        self.allies = listOfPlayers
        self.turnOrder = self.allies + self.enemies
        self.allCharsInFight = self.turnOrder
        self.turnOrder = getTurnOrder(self.turnOrder)


if __name__ == "__main__":
    combat = combatEncounter()
    combat.setUp(6, [Warlock(),Warlock(),Warlock(),Warlock()])


