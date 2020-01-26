from Characters.BaseClass.CharacterBaseClass import Character

# for stats see ghoul dnd 5e

class Shadowling(Character):

    def __init__(self):
        super().__init__()
        self.setStrength(13)
        self.setDex(15)
        self.setConstitution(10)
        self.setInt(7)
        self.setInitiative(2)

        self.setHealth(22)

        self.imagePath = 'assets/images/characters/Enemies/PNG_Images/Shadowling.png'
