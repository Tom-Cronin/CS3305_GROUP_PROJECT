from Characters.BaseClass.CharacterBaseClass import Character
from Characters.attacks.enemyAttacks.sharedAttacks.bite import Bite
from Characters.attacks.enemyAttacks.sharedAttacks.Claws import Claws

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

        self.attack_slot_1 = Bite(self.strength)

        self.attack_slot_2 = Claws(self.strength)

        self.allAttacks = [self.attack_slot_1, self.attack_slot_2]

        self.scale = (30, 30)
        self.imagePath = 'assets/images/characters/Enemies/PNG_Images/rat.png'
        # self.imagePath = 'assets/images/characters/Enemies/PNG_Images/Shadowling.png'
