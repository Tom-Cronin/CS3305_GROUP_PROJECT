from Characters.BaseClass.CharacterBaseClass import Character
from Characters.attacks.playableCharacterAttacks.warlock.DevilishDefence import DevilishDefence
from Characters.attacks.playableCharacterAttacks.warlock.burningSight import BurningSight
from Characters.attacks.playableCharacterAttacks.warlock.eldritchBlast import EldritchBlast
from Characters.attacks.playableCharacterAttacks.warlock.hellfireWhirlwind import HellfireWhirlwind


# will set level to 4 in dnd
 # maybe add a multiplier to health and damge outputs per level

class Warlock(Character):

    def __init__(self):
        super().__init__()
        self.strength = 8
        self.dexterity = 10
        self.constitution = 16
        self.intelligence = 17
        self.ArmorClass = 11
        self.isEnemy = False

        self.setHealth(33)

        self.imagePath = '../assets/images/characters/Enemies/PNG_Images/hag.png'

        self.attack_slot_1 = EldritchBlast(self.intelligence)
        self.attack_slot_2 = DevilishDefence(self.intelligence)
        self.attack_slot_3 = BurningSight(self.intelligence)
        self.attack_slot_4 = HellfireWhirlwind(self.intelligence)


        self.allAttacks = [self.attack_slot_1, self.attack_slot_3, self.attack_slot_4]

        self.name = "Fiend Warlock"
        self.description = "%s\n Health: %i\n Strength: %i\n Dexterity: %i\n Constitution: %i\n Intelligence: %i\n Total Kills: %i\n"

    def updateAttackBonuses(self):
        for attack in self.allAttacks:
            attack.updateDamageMod(self.intelligence)


    def __str__(self):
        return self.description % (self.name, self.health, self.strength,
                                   self.dexterity, self.constitution, self.intelligence, self.totalKills)

