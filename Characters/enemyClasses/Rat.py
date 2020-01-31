from Characters.BaseClass.CharacterBaseClass import Character

# for stats see dread-rat dnd 5e https://www.dandwiki.com/wiki/Dread_Rat_(5e_Creature)



class Rat(Character):

    def __init__(self):
        super().__init__()
        self.strength = 14
        self.dexterity = 16
        self.constitution = 15
        self.intelligence = 4
        self.ArmorClass = 13

        self.setHealth(22)

        self.imagePath = '../../assets/images/characters/Enemies/PNG_Images/rat.png'
