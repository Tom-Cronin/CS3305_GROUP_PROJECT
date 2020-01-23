from Characters.BaseClass.CharacterBaseClass import Character
# for stats see shadow mastiff dnd 5e

class Shadowling(Character):

    def __init__(self):
        super().__init__()
        self.setStrength(16)
        self.setDex(14)
        self.setConstitution(13)
        self.setInt(5)
        self.setInitiative(1)

        self.setHealth(33)

        self.imagePath = 'assets/images/characters/Enemies/PNG_Images/ShadowJest.png'
