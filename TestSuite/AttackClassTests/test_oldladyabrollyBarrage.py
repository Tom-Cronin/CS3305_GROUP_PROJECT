from unittest import TestCase
from Characters.attacks.playableCharacterAttacks.oldLady.BrollyBarrage import BrollyBarrage
from Characters.playerClasses.oldLady import OldLady
class TestFuriousSlashAttack(TestCase):

    def test_get_damage(self):
        person = OldLady()
        hit = BrollyBarrage(person.strength)

        self.assertEqual(18, hit.calcDamage())

