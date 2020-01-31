from Characters.BaseClass.CharacterBaseClass import Character

# for stats see ghoul dnd 5e

class Shadowling(Character):

    def __init__(self):
        super().__init__()
        self.strength = 13
        self.dexterity = 15
        self.constitution = 10
        self.intelligence = 7
        self.ArmorClass = 12

        self.setHealth(22)

        self.imagePath = 'assets/images/characters/Enemies/PNG_Images/Shadowling.png'
