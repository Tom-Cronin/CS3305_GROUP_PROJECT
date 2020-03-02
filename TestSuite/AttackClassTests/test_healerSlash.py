from unittest import TestCase
from Characters.attacks.playableCharacterAttacks.healer.SlashAttack import Slash
from Characters.playerClasses.healer import Healer
class TestFuriousSlashAttack(TestCase):

    def test_get_damage(self):
        person = Healer()
        hit = Slash(person.strength)

        self.assertEqual(5, hit.calcDamage())

