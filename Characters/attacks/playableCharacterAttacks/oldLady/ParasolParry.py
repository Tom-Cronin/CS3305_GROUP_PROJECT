from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus

class ParasolParry(BaseAttack):
    def __init__(self, characterConAtribute):
        super().__init__()
        self.damageMod = calc_attribute_bonus(characterConAtribute)
        self.audioPath = 'none yet'
        self.baseDamage = 2

        self.name = 'ParasolParry'
        self.description = "%s:\nyou enter a fighting stance and parry attacks agaisnt you .\n" \
                           " The target takes %2 physical damage."
        self.coolDown = 3



    def calcDamage(self):
        return self.baseDamage + self.damageMod



    def __str__(self):
        return self.description % (self.name, self.calcDamage())