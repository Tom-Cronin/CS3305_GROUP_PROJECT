from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus


class Longbow(BaseAttack):
    def __init__(self, characterStrength):
        super().__init__()
        self.damageMod = calc_attribute_bonus(characterStrength)
        self.audioPath = 'none yet'
        self.baseDamage = 4

        self.name = 'Longbow'
        self.coolDown = 3
