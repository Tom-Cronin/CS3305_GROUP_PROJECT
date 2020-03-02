from unittest import TestCase
from Characters.attacks.playableCharacterAttacks.healer.TendingWoundsAttack import TendingWounds
from Characters.playerClasses.healer import Healer
class TestFuriousSlashAttack(TestCase):

    def test_get_damage(self):
        person = Healer()
        hit = TendingWounds(person.intelligence)

        self.assertEqual(11, hit.calcDamage())

