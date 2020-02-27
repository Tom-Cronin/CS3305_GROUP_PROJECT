from unittest import TestCase
from Characters.attacks.playableCharacterAttacks.fighter.PowerThoughAttack import PowerThough
from Characters.playerClasses.fighter import Fighter
class TestPowerThoughAttack(TestCase):

    def test_get_damage(self):
        person = Fighter()
        heal = PowerThough(person.constitution)

        self.assertEqual(-2, heal.calcDamage())