from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus
class Slash(BaseAttack):
    def __init__(self, characterStrAtribute):
        super().__init__()
        self.damageMod = calc_attribute_bonus(characterStrAtribute)
        self.audioPath = 'none yet'
        self.baseDamage = 3


        self.name = 'Slash'
        self.description = '%s:\nyou lunge forwards slashing your claws .\n' \
                           ' dealing  %i physical damage to a target.'
        self.coolDown = 1




    def calcDamage(self):
        return self.baseDamage + self.damageMod



    def __str__(self):
        return self.description % (self.name, self.calcDamage())

