from unittest import TestCase
from Characters.attacks.playableCharacterAttacks.fighter.AcidSplashAttack import AcidSplash
from Characters.playerClasses.fighter import Fighter

class TestAcidSplashAttack(TestCase):

    def test_get_damage(self):
        person = Fighter()
        attack = AcidSplash()
        self.assertEqual(4, attack.calcDamage())




