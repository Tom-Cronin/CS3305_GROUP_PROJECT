from CombatSystem.generateEnemies import generateEnemies
from CombatSystem.turnOrder import turnOrder as getTurnOrder

class combatEncounter(object):
    def __init__(self):
        self.enemies = []
        self.allies = []
        self.turnOrder = []
        self.allCharsInFight = []

    def calcDamage(self, tupleOfdamgeAndChar, char=None, boss=False):
        death = False
        attack = tupleOfdamgeAndChar[0]
        playerChar = char
        Damage = attack.calcDamage()
        global enemies, turnOrder, allies
        if attack.isAOE:
            death = False
            for char in self.allies:
                char.takeDamage(Damage)
                if char.health <= 0:
                    death = True
                    self.allies.remove(char)
                    self.turnOrder.remove(char)
                    self.allCharsInFight.remove(char)
            return death

        charTakingDamage = tupleOfdamgeAndChar[1]

        if charTakingDamage == "self":
            playerChar.heal(Damage)
            return death
        elif charTakingDamage == "all":
            for char in self.allies:
                char.heal(Damage)
            return death

        charTakingDamage.takeDamage(Damage)
        if boss and charTakingDamage.health > 0:
            redraw =  charTakingDamage.checkImageChange()
            return redraw
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


    def setUp(self, crChalengeLevel, listOfPlayers, Boss=False):
        self.enemies = generateEnemies(crChalengeLevel, Boss)
        self.allies = listOfPlayers
        self.turnOrder = self.allies + self.enemies
        self.allCharsInFight = self.turnOrder
        self.turnOrder = getTurnOrder(self.turnOrder)
        for char in self.turnOrder:
            char.TurnOrderPosOfEnemys = self.turnOrder.index(char)




