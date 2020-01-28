from Characters.BaseClass.CharacterBaseClass import Character

# for stats see Wight dnd 5e



class Hag(Character):

    def __init__(self):
        super().__init__()
        self.setStrength(15)
        self.setDex(14)
        self.setConstitution(16)
        self.setInt(10)
        self.setInitiative(2)

        self.setHealth(45)

        self.imagePath = 'assets/images/characters/Enemies/PNG_Images/hag.png'
