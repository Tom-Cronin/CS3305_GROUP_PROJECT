from Characters.BaseClass.CharacterBaseClass import Character


 # will set level to 4 in dnd
 # maybe add a multiplier to health and damge outputs per level

class Fighter(Character):

    def __init__(self):
        super().__init__()
        self.strength = 16
        self.dexterity = 12
        self.constitution = 17
        self.intelligence = 8
        self.ArmorClass = 11

        self.setHealth(37)

        self.imagePath = 'none yet'

        self.attack_slot_1 = None
        self.attack_slot_2 = None
        self.attack_slot_3 = None
        self.attack_slot_4 = None


        self.allAttacks = [self.attack_slot_1, self.attack_slot_2]

        self.name = "Fighter"
        self.description = "%s\n Health: %i\n Strength: %i\n Dexterity: %i\n Constitution: %i\n Intelligence: %i\n"

    def updateAttackBonuses(self):
        for attack in self.allAttacks:
            attack.updateDamageMod(self.strength)


    def __str__(self):
        return self.description % (self.name, self.health, self.strength,
                                   self.dexterity, self.constitution, self.intelligence)
