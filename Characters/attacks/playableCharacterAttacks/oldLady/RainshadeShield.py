from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus

class RainshadeShield(BaseAttack):
    def __init__(self, characterConAtribute):
        super().__init__()
        self.damageMod = calc_attribute_bonus(characterConAtribute)
        self.audioPath = 'none yet'
        self.baseDamage = 0

        self.name = 'Rainshade Shield'
        self.description = "%s:\n you rinse your umbrella in front of you rising your defence.\n" \
                           "on self, double your armour class."
        self.coolDown = 5



    def calcDamage(self):
        return self.baseDamage + self.damageMod


    def __str__(self):
        return self.description % (self.name, self.calcDamage())