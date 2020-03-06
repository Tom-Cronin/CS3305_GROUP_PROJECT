from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus

class DoubleSwing(BaseAttack):
    def __init__(self, characterStrAtribute):
        super().__init__()
        self.damageMod = calc_attribute_bonus(characterStrAtribute)
        self.audioPath = 'none yet'
        self.baseDamage = 2

        self.name = 'DoubleStrike'
        self.description = '%s:\n you swing your sword twice in rapid succession.\n' \
                           ' On hit, the target takes %i physical damage.'
        self.coolDown = 1



    def calcDamage(self):
        hit = self.baseDamage + self.damageMod
        doublehit = hit *2
        return doublehit


    def __str__(self):
        return self.description % (self.name, self.calcDamage())

