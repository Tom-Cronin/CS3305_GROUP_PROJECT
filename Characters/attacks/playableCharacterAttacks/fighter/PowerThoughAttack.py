from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus
class PowerThough(BaseAttack):
    def __init__(self, characterConAtribute):
        super().__init__()
        self.damageMod = calc_attribute_bonus(characterConAtribute)
        self.audioPath = 'none yet'
        self.baseDamage = 4
        self.baseHeal = -5

        self.name = 'Power Though'
        self.description = '%s:\nyou battle though the pain .\n' \
                           ' On self, healing your self for %i health.'
        self.cooldown = 3




    def calcDamage(self):
        return self.baseHeal + self.damageMod



    def __str__(self):
        return self.description % (self.name, self.calcDamage())

