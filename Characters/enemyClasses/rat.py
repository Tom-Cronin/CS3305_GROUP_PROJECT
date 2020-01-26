from Characters.BaseClass.CharacterBaseClass import Character

# for stats see dread-rat dnd 5e https://www.dandwiki.com/wiki/Dread_Rat_(5e_Creature)



class Hag(Character):

    def __init__(self):
        super().__init__()
        self.setStrength(14)
        self.setDex(16)
        self.setConstitution(15)
        self.setInt(4)
        self.setInitiative(3)

        self.setHealth(22)

        self.imagePath = 'assets/images/characters/Enemies/PNG_Images/rat.png'
