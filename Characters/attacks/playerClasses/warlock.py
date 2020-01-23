from Characters.BaseClass.CharacterBaseClass import Character
from Characters.attacks.playableCharacterAttacks.warlock.DevilishDefence import DevilishDefence
from Characters.attacks.playableCharacterAttacks.warlock.eldritchBlast import EldritchBlast

 # will set level to 4 in dnd
 # maybe add a multiplier to health and damge outputs per level

class Warlock(Character):

    def __init__(self):
        super().__init__()
        self.setStrength(8)
        self.setDex(10)
        self.setConstitution(16)
        self.setInt(17)
        self.setInitiative(0)

        self.setHealth(33)

        self.imagePath = 'none yet'

        self.attack1 = EldritchBlast(self.getInt())
        self.attack2 = DevilishDefence(self.getInt())

    def attack(self, attackSlotNumber):
        attacks = {
            1: self.attack1,
            2: self.attack2
        }
        return attacks.get(attackSlotNumber)

warlock  = Warlock()
warlock.attack(1).attack()
