from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus
class HeavySwing(BaseAttack):
    def __init__(self, characterStrAtribute):
        super().__init__()
        self.damageMod = calc_attribute_bonus(characterStrAtribute)

        self.audioPath = 'none yet'
        self.baseDamage = 8

        self.name = 'HeavySwing'
        self.description = '%s:\n you rise your sword higg in to the air and swing with unstoppable force.\n' \
                           ' On hit, the target takes %i physical damage.'
        self.coolDown = 4



    def calcDamage(self):
        return self.baseDamage + self.damageMod



    def __str__(self):
        return self.description % (self.name, self.calcDamage())

