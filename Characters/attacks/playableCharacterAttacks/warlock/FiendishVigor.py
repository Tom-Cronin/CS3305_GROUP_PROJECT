from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus


class Vigor(BaseAttack):
    def __init__(self, characterIntAtribute):
        super().__init__()
        self.damageMod =  calc_attribute_bonus(characterIntAtribute)
        self.baseDamage = 10
        self.name = 'Fiendish Vigor'
        self.isHeal = True
        self.healType = "self"
        self.description = '%s:\n You create a field of magical energy around yourself.\n' \
                           ' Your AC is increased by %i for 3 turns'
        self.coolDown = 2


    def __str__(self):
        return self.description % (self.name, self.calcDamage())
