from Characters.BaseClass.CharacterBaseClass import Character
# for stats see night hag, flesh golem, zombie beholder, or a warlock of great old one dnd 5e

#TODO get the stats and finalise it


class GateGuard(Character):

    def __init__(self):
        super().__init__()
        self.strength(15)
        self.dexterity(14)
        self.constitution(16)
        self.intelligence(10)
        self.ArmorClass(15)

        self.setHealth(45)

        self.imagePath = 'assets/images/characters/Enemies/PNG_Images/hag.png'
