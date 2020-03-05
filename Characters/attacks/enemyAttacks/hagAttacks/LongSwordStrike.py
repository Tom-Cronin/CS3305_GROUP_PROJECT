from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus


class twoHanded(BaseAttack):
    def __init__(self, characterStrength):
        super().__init__()
        self.damageMod = calc_attribute_bonus(characterStrength)
        self.audioPath = 'none yet'
        self.baseDamage = 5

        self.name = 'Longsword two handed strike'
        self.coolDown = 4


    def calcDamage(self):
        return self.baseDamage + self.damageMod


class oneHanded(BaseAttack):
    def __init__(self, characterStrength):
        super().__init__()
        self.damageMod = calc_attribute_bonus(characterStrength)
        self.audioPath = 'none yet'
        self.baseDamage = 4

        self.name = 'Longsword one handed strike'
        self.coolDown = 3


