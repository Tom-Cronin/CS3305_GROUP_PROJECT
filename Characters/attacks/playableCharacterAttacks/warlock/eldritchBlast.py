from Characters.attacks.baseAttackClass import BaseAttack

class EldritchBlast(BaseAttack):
    def __init__(self, characterIntAtribute):
        super().__init__()
        super.damageMod = characterIntAtribute
        self.baseDamage = 10
        self.name = 'Eldritch Blast'
        self.description = 'You create a beam of magical energy and hurl it at an enemy.' \
                           'On hit, the target takes %i necrotic damage.'

    def updateDamageMod(self, newDamageMod):
        self.damageMod = newDamageMod

    def __str__(self):
        return self.description % (self.getDamage())

