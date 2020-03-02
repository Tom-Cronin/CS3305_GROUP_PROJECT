from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus


class Club(BaseAttack):
    def __init__(self, characterStrength):
        super().__init__()
        self.damageMod = calc_attribute_bonus(characterStrength)
        self.audioPath = 'none yet'
        self.baseDamage = 12

        self.name = 'Club Swing'
        self.coolDown = 3
