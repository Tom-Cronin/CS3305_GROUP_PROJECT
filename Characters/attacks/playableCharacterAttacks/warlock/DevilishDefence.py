from Characters.attacks.baseAttackClass import BaseAttack

class DevilishDefence(BaseAttack):
    def __init__(self, characterIntAtribute):
        super().__init__()
        self.damageMod = characterIntAtribute
        self.baseDamage = 0
        self.name = 'Devilish Defence'
        self.description = 'You create a field of magical energy around yourself.' \
                           'Your AC is increased by %i for 3 turns'
        self.coolDown = 4
        self.duration = 3

    def updateDamageMod(self, newDamageMod):
        self.damageMod = newDamageMod

    def __str__(self):
        return self.description % (self.getDamage())
