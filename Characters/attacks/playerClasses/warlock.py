from Characters.BaseClass.CharacterBaseClass import Character

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

# 4 attakcs
# normal strike [common to all ]
# eldritch blast [ will do 10 + 1 per level damage ]
# burningFire (burning hands)
# invisibity [ will let you skip for one round ] cooldown 3 rounds