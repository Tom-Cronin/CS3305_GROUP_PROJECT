from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus
class FuriousSlash(BaseAttack):
    def __init__(self, characterStrAtribute):
        super().__init__()
        self.damageMod = calc_attribute_bonus(characterStrAtribute)
        self.audioPath = 'none yet'
        self.baseDamage = 5


        self.name = 'Tending Wounds'
        self.description = '%s:\nyou swing with wild ferocity  .\n' \
                           ' On target,  you deal %i physical damage.'
        self.coolDown = 3




    def calcDamage(self):
        return self.baseDamage + self.damageMod



    def __str__(self):
        return self.description % (self.name, self.calcDamage())

