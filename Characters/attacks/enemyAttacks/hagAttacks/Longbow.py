from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus


class Longbow(BaseAttack):
    def __init__(self, characterStrength):
        super().__init__()
        self.damageMod = calc_attribute_bonus(characterStrength)
        self.audioPath = 'none yet'
        self.baseDamage = 4

        self.name = 'Longbow'
        self.cooldown = 3



    def calcDamage(self):
        return self.baseDamage + self.damageMod

    def attack(self):
        #self.playAttackSound(self.audioPath)
        print(self.getDamage())