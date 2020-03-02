from Characters.attacks.baseAttackClass import BaseAttack
from Characters.sharedFunctions import calc_attribute_bonus

class GlorPres(BaseAttack):
    def __init__(self, characterConAtribute):
        super().__init__()
        self.damageMod = calc_attribute_bonus(characterConAtribute)
        self.audioPath = 'none yet'
        self.baseDamage = 20

        self.name = 'Glorious Presence'
        self.isHeal = True
        self.healType = "all"
        self.description = "Your beauty and elegance inspire all, yourself included, healing everyone %i health"
        self.coolDown = 4



    def calcDamage(self):
        return self.baseDamage + self.damageMod


    def __str__(self):
        return self.description % (self.name, self.calcDamage())