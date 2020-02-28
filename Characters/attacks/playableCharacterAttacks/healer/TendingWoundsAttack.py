from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus
class TendingWounds(BaseAttack):
    def __init__(self, characterIntAtribute):
        super().__init__()
        self.damageMod = calc_attribute_bonus(characterIntAtribute)
        self.audioPath = 'none yet'
        self.baseDamage = 0
        self.baseHeal = -7

        self.name = 'Tending Wounds'
        self.description = '%s:\nyou treat your hurts.\n' \
                           ' On self, healing your self for %i health.'
        self.coolDown = 2




    def calcDamage(self):
        return self.baseHeal


    def __str__(self):
        return self.description % (self.name, self.calcDamage())

