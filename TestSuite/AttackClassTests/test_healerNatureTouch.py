from unittest import TestCase
from Characters.attacks.playableCharacterAttacks.healer.NaturesTouchAttack import NaturesTouch
from Characters.playerClasses.healer import Healer
class TestFuriousSlashAttack(TestCase):

    def test_get_damage(self):
        person = Healer()
        hit = NaturesTouch(person.intelligence)

        self.assertEqual(-4, hit.calcDamage())

