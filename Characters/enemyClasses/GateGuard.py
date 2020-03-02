from Characters.BaseClass.CharacterBaseClass import Character
from Characters.attacks.enemyAttacks.gateGuardAttacks import Club,PoisonBreath,slam, ArcaneExplosion
# for stats see night hag, flesh golem, zombie beholder, or a warlock of great old one dnd 5e

#TODO get the stats and finalise it


class GateGuard(Character):

    def __init__(self):
        super().__init__()
        self.strength = 19
        self.dexterity = 14
        self.constitution = 18
        self.intelligence = 3
        self.ArmorClass = 12
        self.isEnemy =True
        self.setHealth(110)

        self.attack_slot_1 = Club.Club(self.strength)
        self.attack_slot_2 = PoisonBreath.PoisonBreath(self.strength)
        self.attack_slot_3 = slam.Slam(self.strength)
        self.attack_slot_4 = None

        self.stagePositionY = 85
        self.stagePositionX = 70

        self.allAttacks = [self.attack_slot_1, self.attack_slot_2, self.attack_slot_3]

        self.scale = (495, 495)
        self.name = "Iron Golem"
        self.imagePath = 'assets/images/characters/Players/PNG_Images/IronBoss/Golem1.png'

    def checkImageChange(self):
            if (self.maxHealth // 3 + self.maxHealth // 3) >= self.health > (self.maxHealth // 3):
                self.imagePath = 'assets/images/characters/Players/PNG_Images/IronBoss/Golem2.png'
                return True
            elif  self.health <= (self.maxHealth//3):
                self.imagePath = 'assets/images/characters/Players/PNG_Images/IronBoss/Golem3.png'
                self.attack_slot_4 = ArcaneExplosion.ArcaneExplosion(10)
                self.allAttacks.append(self.attack_slot_4)
                return True
            return False

