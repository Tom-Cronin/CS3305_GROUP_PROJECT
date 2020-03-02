from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus


class PoisonBreath(BaseAttack):
    def __init__(self, characterStrength):
        super().__init__()
        self.damageMod = calc_attribute_bonus(characterStrength)
        self.audioPath = 'none yet'
        self.baseDamage = 10
        self.isAOE = True


        self.name = 'Poison Breath'
        self.coolDown = 4




