from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus

class HellfireWhirlwind(BaseAttack):
    def __init__(self, characterIntAtribute):
        super().__init__()
        self.damageMod = calc_attribute_bonus(characterIntAtribute)
        self.audioPath = 'none yet'
        self.baseDamage = 8

        self.name = 'Hellfire Whirlwind'
        self.description = '%s:\n You surround and enemy in a whirlwind of hellfire .\n' \
                           ' On hit, the target takes %i fire damage.'
        self.cooldown = 2



    def calcDamage(self):
        return self.baseDamage + self.damageMod

    def attack(self):
        #self.playAttackSound(self.audioPath)
        print(self.getDamage())

    def __str__(self):
        return self.description % (self.name, self.getDamage())