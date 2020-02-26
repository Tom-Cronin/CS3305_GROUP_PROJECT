from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus


class HellfireWhirlwind(BaseAttack):
    def __init__(self, characterIntAtribute):
        super().__init__()
        self.damageMod = calc_attribute_bonus(characterIntAtribute)
        self.audioPath = 'none yet'
        self.baseDamage = 5

        self.name = 'Hellfire Whirlwind'
        self.description = 'You surround and enemy in a whirlwind of hellfire.\n ' \
                           'On hit, the target takes %i fire damage.'
        self.AllDetails = '%s:\n %s' % (self.name, self.description)
        self.coolDown = 4

    def calcDamage(self):
        return self.baseDamage + self.damageMod


    def __str__(self):
        return self.AllDetails % (self.getDamage())
