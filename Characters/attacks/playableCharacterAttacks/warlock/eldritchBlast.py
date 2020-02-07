from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus


class EldritchBlast(BaseAttack):
    def __init__(self, characterIntAtribute):
        super().__init__()
        self.damageMod = calc_attribute_bonus(characterIntAtribute)
        self.audioPath = '../../assets/images/sounds/Warlock/eldritchBlast.mp3'
        self.baseDamage = 99

        self.name = 'Eldritch Blast'
        self.description = '%s:\n You create a beam of magical energy and hurl it at an enemy.\n' \
                           ' On hit, the target takes %i fire damage.'
        self.coolDown = 1



    def calcDamage(self):
        return self.baseDamage + self.damageMod

    def attack(self):
        self.playAttackSound(self.audioPath)
        print(self.getDamage())

    def __str__(self):
        return self.description % (self.name, self.getDamage())

