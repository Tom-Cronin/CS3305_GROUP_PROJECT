from Characters.BaseClass.CharacterBaseClass import Character
from Characters.attacks.enemyAttacks.sharedAttacks.bite import Bite
from Characters.attacks.enemyAttacks.sharedAttacks.Claws import Claws
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

        self.attack_slot_1 = Bite(self.dexterity)
        self.attack_slot_1.coolDown = 2
        self.attack_slot_1.baseDamage = 4

        self.attack_slot_2 = Claws(self.dexterity)
        self.attack_slot_2.baseDamage = 3

        self.allAttacks = [self.attack_slot_1, self.attack_slot_2]

        self.imagePath = 'assets/images/characters/Enemies/PNG_Images/rat.png'
