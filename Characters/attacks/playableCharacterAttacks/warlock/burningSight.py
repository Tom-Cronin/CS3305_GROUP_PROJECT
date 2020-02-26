from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus

class BurningSight(BaseAttack):
    def __init__(self, characterIntAtribute):
        super().__init__()
        self.damageMod = calc_attribute_bonus(characterIntAtribute)
        self.audioPath = 'none yet'
        self.baseDamage = 4

        self.name = 'Burning Sight'
        self.description = "%s:\n You gaze into your enemy's eyes as their eyelids begin to burn.\n" \
                           " The target takes %i fire damage."
        self.coolDown = 2



    def calcDamage(self):
        return self.baseDamage + self.damageMod



    def __str__(self):
        return self.description % (self.name, self.getDamage())