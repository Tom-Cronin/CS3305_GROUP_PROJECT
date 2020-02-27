from unittest import TestCase
from Characters.attacks.playableCharacterAttacks.fighter.HeavySwingAttack import HeavySwing
from Characters.playerClasses.fighter import Fighter

class TestHeavySwingAttack(TestCase):

    def test_get_damage(self):
        person = Fighter()
        attack = HeavySwing(person.strength)

        self.assertEqual(11, attack.calcDamage())