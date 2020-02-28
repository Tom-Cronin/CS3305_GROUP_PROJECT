from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus

class UmbrellaSmash(BaseAttack):
    def __init__(self, characterStrAtribute):
        super().__init__()
        self.damageMod = calc_attribute_bonus(characterStrAtribute)
        self.audioPath = 'none yet'
        self.baseDamage = 4

        self.name = 'Umbrella Smash'
        self.description = "%s:\nyou smash your umbrella hard agaisnt the target  .\n" \
                           "on Target, takes %i physical damage."
        self.coolDown = 1



    def calcDamage(self):
        return self.baseDamage + self.damageMod


    def __str__(self):
        return self.description % (self.name, self.calcDamage())