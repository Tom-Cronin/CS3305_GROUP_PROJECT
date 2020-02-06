from Characters.BaseClass.CharacterBaseClass import Character
from Characters.attacks.enemyAttacks.hagAttacks import lifeDrain, Longbow, LongSwordStrike
# for stats see Wight dnd 5e



class Hag(Character):

    def __init__(self):
        super().__init__()
        self.strength = 15
        self.dexterity = 14
        self.constitution = 16
        self.intelligence = 10
        self.ArmorClass = 14

        self.setHealth(45)

        self.imagePath = 'assets/images/characters/Enemies/PNG_Images/hag.png'

        self.attack_slot_1 = lifeDrain.LifeDrain(self.intelligence)
        self.attack_slot_2 = Longbow.Longbow(self.dexterity)
        self.attack_slot_3 = LongSwordStrike.onoHanded(self.strength)
        self.attack_slot_4 = LongSwordStrike.twoHanded(self.strength)

        self.allAttacks = [self.attack_slot_1, self.attack_slot_2,self.attack_slot_3, self.attack_slot_4]
