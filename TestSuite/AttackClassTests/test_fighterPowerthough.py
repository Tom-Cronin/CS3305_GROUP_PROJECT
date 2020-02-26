from unittest import TestCase
from Characters.attacks.playableCharacterAttacks.fighter.PowerThoughAttack import PowerThough
class TestPowerThoughAttack(TestCase):

    def test_get_damage(self):
        heal = PowerThough()
        self.assertEqual(-5, heal.calcDamage())