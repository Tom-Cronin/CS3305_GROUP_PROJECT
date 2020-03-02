from Characters.BaseClass.CharacterBaseClass import Character
from Characters.attacks.enemyAttacks.sharedAttacks.bite import Bite
from Characters.attacks.enemyAttacks.sharedAttacks.Claws import Claws
# for stats see shadow mastiff dnd 5e

class ShadowJest(Character):

    def __init__(self):
        super().__init__()
        self.strength = 16
        self.dexterity = 14
        self.constitution = 13
        self.intelligence = 5
        self.ArmorClass = 1
        self.name = "Jest"


        self.setHealth(33)

        self.attack_slot_1 = Bite(self.strength)
        self.attack_slot_2 = Claws(self.strength)
        self.attack_slot_2.name = "Slash"

        self.allAttacks = [self.attack_slot_1]

        self.scale = (300, 330)

        self.imagePath = 'assets/images/characters/Enemies/PNG_Images/ShadowJest.png'
        # self.imagePath = 'assets/images/characters/Enemies/PNG_Images/ShadowJest.png'
