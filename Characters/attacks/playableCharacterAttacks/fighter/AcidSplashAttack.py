from Characters.attacks.baseAttackClass import BaseAttack


class AcidSplash(BaseAttack):
    def __init__(self):
        super().__init__()
        self.damageMod = 0
        self.audioPath = 'none yet'
        self.baseDamage = 4

        self.name = 'Acid Splash'
        self.description = '%s:\n You throw a acid flash at the enemy.\n' \
                           ' On hit, the target takes %i acid damage.'
        self.cooldown = 3



    def calcDamage(self):
        return self.baseDamage + self.damageMod



    def __str__(self):
        return self.description % (self.name, self.calcDamage())

