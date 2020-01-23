from Characters.BaseClass.CharacterBaseClass import Character
# for stats see night hag, flesh golem, zombie beholder, or a warlock of great old one dnd 5e

#TODO get the stats and finalise it


class GateGuard(Character):

    def __init__(self):
        super().__init__()
        self.setStrength(15)
        self.setDex(14)
        self.setConstitution(16)
        self.setInt(10)
        self.setInitiative(10)

        self.setHealth(45)

        self.imagePath = 'assets/images/characters/Enemies/PNG_Images/hag.png'
