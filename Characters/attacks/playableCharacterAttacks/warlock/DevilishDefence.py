from Characters.attacks.baseAttackClass import BaseAttack


class DevilishDefence(BaseAttack):
    def __init__(self, characterIntAtribute):
        super().__init__()
        self.damageMod = 0
        self.baseDamage = 0
        self.name = 'Devilish Defence'
        self.description = '%s:\n You create a field of magical energy around yourself.\n' \
                           ' Your AC is increased by %i for 3 turns'
        self.coolDown = 2


    def __str__(self):
        return self.description % (self.name, self.calcDamage())
