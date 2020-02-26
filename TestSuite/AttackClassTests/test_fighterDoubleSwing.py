from unittest import TestCase
from Characters.attacks.playableCharacterAttacks.fighter.DoubleSwingAttack import DoubleSwing

class TestDoubleSwingAttack(TestCase):

    def test_get_damage(self):
        attack = DoubleSwing()
        self.assertEqual(4, attack.calcDamage())