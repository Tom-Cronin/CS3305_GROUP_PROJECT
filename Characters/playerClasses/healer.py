from Characters.BaseClass.CharacterBaseClass import Character

from Characters.attacks.playableCharacterAttacks.healer.furiousSlashAttack import FuriousSlash
from Characters.attacks.playableCharacterAttacks.healer.NaturesTouchAttack import NaturesTouch
from Characters.attacks.playableCharacterAttacks.healer.SlashAttack import Slash
from Characters.attacks.playableCharacterAttacks.healer.TendingWoundsAttack import TendingWounds

class Healer(Character):

    def __init__(self):
        super().__init__()
        self.strength = 14
        self.dexterity = 13
        self.constitution = 15
        self.intelligence = 18
        self.ArmorClass = 10
        self.isEnemy = False

        self.setHealth(31)
        self.scale = (180, 240)
        self.stagePositionY = 340

        self.imagePath = "assets/images/characters/Players/PNG_Images/druid.png"

        self.attack_slot_1 = Slash(self.strength)
        self.attack_slot_2 = FuriousSlash(self.strength)
        self.attack_slot_3 = NaturesTouch(self.intelligence)
        self.attack_slot_4 = TendingWounds(self.intelligence)

        self.nonInitAttacks = [Slash,FuriousSlash,NaturesTouch,TendingWounds]

        self.attackBonus = [self.strength,self.strength, self.intelligence, self.intelligence]




        self.allAttacks = [self.attack_slot_1, self.attack_slot_2, self.attack_slot_3, self.attack_slot_4]


        self.description = "%s\n Health: %i\n Strength: %i\n Dexterity: %i\n Constitution: %i\n Intelligence: %i\n"

    def updateAttackBonuses(self):
        for attack in self.allAttacks:
            attack.updateDamageMod(self.intelligence)

    def updateBonusList(self):
        self.attackBonus = [self.strength,self.strength, self.intelligence, self.intelligence]

    def __str__(self):
        return self.description % (self.name, self.health, self.strength,
                                   self.dexterity, self.constitution, self.intelligence)
