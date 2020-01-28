from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus


class BreathAttack(BaseAttack):
    def __init__(self):
        super().__init__()
        self.damageMod = 0
        self.audioPath = 'none yet'
        self.baseDamage = 4

        self.name = 'Acid Spray'
        self.description = '%s:\n You create a beam of magical energy and hurl it at an enemy.\n' \
                           ' On hit, the target takes %i acid damage.'
        self.cooldown = 3



    def calcDamage(self):
        return self.baseDamage + self.damageMod

    def attack(self):
        #self.playAttackSound(self.audioPath)
        print(self.getDamage())

    def __str__(self):
        return self.description % (self.name, self.getDamage())
