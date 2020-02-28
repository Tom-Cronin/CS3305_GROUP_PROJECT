from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus
class PowerThough(BaseAttack):
    def __init__(self, characterConAtribute):
        super().__init__()
        self.damageMod = calc_attribute_bonus(characterConAtribute)
        self.audioPath = 'none yet'
        self.baseDamage = 6
        self.isHeal = True
        self.healType = "self"

        self.name = 'Power Through'
        self.description = '%s:\nyou battle through the pain .\n' \
                           ' On self, healing your self for %i health.'
        self.coolDown = 3








    def __str__(self):
        return self.description % (self.name, self.calcDamage())

