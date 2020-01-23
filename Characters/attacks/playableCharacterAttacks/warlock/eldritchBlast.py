from Characters.attacks.baseAttackClass import BaseAttack

class EldritchBlast(BaseAttack):
    def __init__(self, characterIntAtribute):
        super().__init__()
        self.damageMod = characterIntAtribute
        self.audioPath = '../../../assets/images/sounds/Warlock/eldritchBlast.mp3'
        self.baseDamage = 10
        self.name = 'Eldritch Blast'
        self.description = 'You create a beam of magical energy and hurl it at an enemy.' \
                           'On hit, the target takes %i fire damage.'
        self.cooldown = 1

    def updateDamageMod(self, newDamageMod):
        self.damageMod = newDamageMod

    def attack(self):
        self.playAttackSound(self.audioPath)
    def __str__(self):
        return self.description % (self.getDamage())

