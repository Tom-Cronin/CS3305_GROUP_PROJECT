from CombatSystem.generateEnemies import generateEnemies
from CombatSystem.turnOrder import turnOrder as getTurnOrder

class combatEncounter(object):
    def __init__(self):
        self.enemies = []
        self.allies = []
        self.turnOrder = []
        self.allCharsInFight = []

    def calcDamage(self, tupleOfdamgeAndChar, char=None):
        death = False
        Damage = tupleOfdamgeAndChar[0]
        charTakingDamage = tupleOfdamgeAndChar[1]
        global enemies, turnOrder, allies
        charTakingDamage.takeDamage(Damage)
        if charTakingDamage.health <= 0:
            death = True
            if charTakingDamage.isEnemy:
                self.enemies.remove(charTakingDamage)
                char.killCounter()
            else:
                self.allies.remove(charTakingDamage)
            self.turnOrder.remove(charTakingDamage)
            self.allCharsInFight.remove(charTakingDamage)
            del charTakingDamage
        return death


    def setUp(self, crChalengeLevel, listOfPlayers):
        self.enemies = generateEnemies(crChalengeLevel)
        self.allies = listOfPlayers
        self.turnOrder = self.allies + self.enemies
        self.allCharsInFight = self.turnOrder
        self.turnOrder = getTurnOrder(self.turnOrder)
        for char in self.turnOrder:
            char.TurnOrderPosOfEnemys = self.turnOrder.index(char)




