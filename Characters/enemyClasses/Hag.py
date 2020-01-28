from Characters.BaseClass.CharacterBaseClass import Character

# for stats see Wight dnd 5e



class Hag(Character):

    def __init__(self):
        super().__init__()
        self.strength(15)
        self.dexterity(14)
        self.constitution(16)
        self.intelligence(10)
        self.ArmorClass(14)

        self.setHealth(45)

        self.imagePath = 'assets/images/characters/Enemies/PNG_Images/hag.png'
