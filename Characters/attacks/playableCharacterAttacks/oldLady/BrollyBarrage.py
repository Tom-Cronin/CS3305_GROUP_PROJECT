from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus

class BrollyBarrage(BaseAttack):
    def __init__(self, characterStrAtribute):
        super().__init__()
        self.damageMod = calc_attribute_bonus(characterStrAtribute)
        self.audioPath = 'none yet'
        self.baseDamage = 3

        self.name = 'Brolly Barrage'
        self.description = "%s:\n you unleast a barrage of brolly blows.\n" \
                           " The target takes %i physical damage."
        self.coolDown = 4



    def calcDamage(self):
        hit = self.baseDamage + self.damageMod
        hit = hit *3
        return hit



    def __str__(self):
        return self.description % (self.name, self.calcDamage())