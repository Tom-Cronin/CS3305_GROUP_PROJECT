from unittest import TestCase
from Characters.attacks.playableCharacterAttacks.fighter.HeavySwingAttack import HeavySwing
class TestHeavySwingAttack(TestCase):

    def test_get_damage(self):
        attack = HeavySwing()
        self.assertEqual(7, attack.calcDamage())