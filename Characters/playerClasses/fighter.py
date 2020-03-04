from Characters.BaseClass.CharacterBaseClass import Character
from Characters.attacks.playableCharacterAttacks.fighter.AcidSplashAttack import AcidSplash
from Characters.attacks.playableCharacterAttacks.fighter.DoubleSwingAttack import DoubleSwing
from Characters.attacks.playableCharacterAttacks.fighter.HeavySwingAttack import HeavySwing
from Characters.attacks.playableCharacterAttacks.fighter.PowerThoughAttack import PowerThough


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
        self.isEnemy = False

        self.setHealth(37)

        self.imagePath = None

        self.attack_slot_1 = AcidSplash()
        self.attack_slot_2 = DoubleSwing(self.strength)
        self.attack_slot_3 = HeavySwing(self.strength)
        self.attack_slot_4 = PowerThough(self.constitution)

        self.nonInitAttacks = [AcidSplash,DoubleSwing,HeavySwing,PowerThough]

        self.attackBonus = ["optional", self.strength, self.strength,self.constitution]

        self.scale = (220, 300)
        self.stagePositionY = 280


        self.allAttacks = [self.attack_slot_1, self.attack_slot_2, self.attack_slot_3, self.attack_slot_4]


        self.imagePath = 'assets/images/characters/Players/PNG_Images/Knight.png'
        self.description = "%s\n Health: %i\n Strength: %i\n Dexterity: %i\n Constitution: %i\n Intelligence: %i\n"

    def updateAttackBonuses(self):
        for attack in self.allAttacks:
            attack.updateDamageMod(self.strength)

    def updateBonusList(self):
        self.attackBonus = ["optional", self.strength, self.strength,self.constitution]

    def __str__(self):
        return self.description % (self.name, self.health, self.strength,
                                   self.dexterity, self.constitution, self.intelligence)
