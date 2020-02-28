from unittest import TestCase
from Characters.attacks.playableCharacterAttacks.fighter.DoubleSwingAttack import DoubleSwing
from Characters.playerClasses.fighter import Fighter
from Characters.attacks.baseAttackClass import BaseAttack

class TestDoubleSwingAttack(TestCase):

    def test_get_damage(self):
        perosn = Fighter()
        attack = DoubleSwing(perosn.strength)

        self.assertEqual(10, attack.calcDamage())