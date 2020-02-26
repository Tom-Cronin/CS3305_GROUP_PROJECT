from Characters.BaseClass.CharacterBaseClass import Character
from Characters.attacks.enemyAttacks.sharedAttacks.bite import Bite
# for stats see shadow mastiff dnd 5e

class ShadowJest(Character):

    def __init__(self):
        super().__init__()
        self.strength = 16
        self.dexterity = 14
        self.constitution = 13
        self.intelligence = 5
        self.ArmorClass = 1

        self.setHealth(33)

        self.attack_slot_1 = Bite(self.strength)

        self.allAttacks = [self.attack_slot_1]

        self.scale = (30, 30)
        self.imagePath = 'assets/images/characters/Enemies/PNG_Images/rat.png'
        # self.imagePath = 'assets/images/characters/Enemies/PNG_Images/ShadowJest.png'
