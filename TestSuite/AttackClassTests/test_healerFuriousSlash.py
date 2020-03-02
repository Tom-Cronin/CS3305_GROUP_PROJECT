from unittest import TestCase
from Characters.attacks.playableCharacterAttacks.healer.furiousSlashAttack import FuriousSlash
from Characters.playerClasses.healer import Healer
class TestFuriousSlashAttack(TestCase):

    def test_get_damage(self):
        person = Healer()
        hit = FuriousSlash(person.strength)

        self.assertEqual(7, hit.calcDamage())

