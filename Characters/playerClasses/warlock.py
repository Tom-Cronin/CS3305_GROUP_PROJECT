from Characters.BaseClass.CharacterBaseClass import Character
from Characters.attacks.playableCharacterAttacks.warlock.FiendishVigor import Vigor
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

        self.setHealth(27)

        self.attackSoundPath = "assets/sounds/Warlock/eldritchBlast.mp3"
        self.imagePath = 'assets/images/characters/Players/PNG_Images/W_Of_F.png'

        self.attack_slot_1 = EldritchBlast(self.intelligence)
        self.attack_slot_2 = Vigor(self.intelligence)
        self.attack_slot_3 = BurningSight(self.intelligence)
        self.attack_slot_4 = HellfireWhirlwind(self.intelligence)
        self.nonInitAttacks = [EldritchBlast,Vigor,BurningSight,HellfireWhirlwind]
        self.attackBonus = (self.intelligence, self.intelligence,self.intelligence,self.intelligence)


        self.allAttacks = [self.attack_slot_1, self.attack_slot_2, self.attack_slot_3, self.attack_slot_4]
        self.scale = (180, 240)
        self.stagePositionY = 350


        self.description = "%s\n Health: %i\n Strength: %i\n Dexterity: %i\n " \
                           "Constitution: %i\n Intelligence: %i\n Total Kills: %i\n"

    def updateAttackBonuses(self):
        for attack in self.allAttacks:
            attack.updateDamageMod(self.intelligence)

    def updateBonusList(self):
        self.attackBonus = (self.intelligence, self.intelligence, self.intelligence, self.intelligence)

    def __str__(self):
        return self.description % (self.name, self.health, self.strength,
                                   self.dexterity, self.constitution, self.intelligence, self.totalKills)

