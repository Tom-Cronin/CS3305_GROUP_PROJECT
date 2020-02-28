from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus
class NaturesTouch(BaseAttack):
    def __init__(self, characterIntAtribute):
        super().__init__()

        self.damageMod = calc_attribute_bonus(characterIntAtribute)
        self.audioPath = 'none yet'
        self.baseDamage = 0
        self.baseHeal = -4

        self.name = 'Natures Touch'
        self.description = '%s:\nyou feel nature grasp healing you and your allies  .\n' \
                           'healing you and your allies for %i health.'
        self.coolDown = 2




    def calcDamage(self):
        return self.baseHeal



    def __str__(self):
        return self.description % (self.name, self.calcDamage())

