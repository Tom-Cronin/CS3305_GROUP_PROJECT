from unittest import TestCase
from Characters.attacks.playableCharacterAttacks.oldLady.UmbrellaSmash import UmbrellaSmash
from Characters.playerClasses.oldLady import OldLady
class TestFuriousSlashAttack(TestCase):

    def test_get_damage(self):
        person = OldLady()
        hit = UmbrellaSmash(person.strength)

        self.assertEqual(7, hit.calcDamage())

