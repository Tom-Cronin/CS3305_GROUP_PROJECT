from Characters.BaseClass.CharacterBaseClass import Character

from Characters.attacks.playableCharacterAttacks.oldLady.BrollyBarrage import BrollyBarrage
from Characters.attacks.playableCharacterAttacks.oldLady.UmbrellaSmash import UmbrellaSmash
from Characters.attacks.playableCharacterAttacks.oldLady.RainshadeShield import GlorPres
from Characters.attacks.playableCharacterAttacks.oldLady.ParasolParry import ParasolParry


class OldLady(Character):

    def __init__(self):
        super().__init__()
        self.strength = 17
        self.dexterity = 14
        self.constitution = 16
        self.intelligence = 13
        self.ArmorClass = 12
        self.isEnemy = False

        self.setHealth(35)
        self.scale = (110, 240)
        self.stagePositionY = 360
        self.imagePath = "assets/images/characters/Players/PNG_Images/CrazyLady.png"

        self.attack_slot_1 = UmbrellaSmash(self.strength)
        self.attack_slot_2 = BrollyBarrage(self.strength)
        self.attack_slot_3 = ParasolParry(self.constitution)
        self.attack_slot_4 = GlorPres(self.constitution)
        self.attack_slot_4.name = "Demo Kill"
        self.attack_slot_4.baseDamage = 99999
        self.attack_slot_4.coolDown = 0
        self.attack_slot_4.isHeal = False


        self.allAttacks = [self.attack_slot_1, self.attack_slot_2, self.attack_slot_3, self.attack_slot_4]


        self.description = "%s\n Health: %i\n Strength: %i\n Dexterity: %i\n Constitution: %i\n Intelligence: %i\n"

    def updateAttackBonuses(self):
        for attack in self.allAttacks:
            attack.updateDamageMod(self.intelligence)

    def __str__(self):
        return self.description % (self.name, self.health, self.strength,
                                   self.dexterity, self.constitution, self.intelligence)
