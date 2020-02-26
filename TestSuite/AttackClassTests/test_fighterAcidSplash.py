from unittest import TestCase
from Characters.attacks.playableCharacterAttacks.fighter.AcidSplashAttack import AcidSplash

class TestAcidSplashAttack(TestCase):

    def test_get_damage(self):
        attack = AcidSplash()
        self.assertEqual(4, attack.calcDamage())




