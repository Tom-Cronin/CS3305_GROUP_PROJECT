from unittest import TestCase
from Characters.attacks.playableCharacterAttacks.oldLady.ParasolParry import ParasolParry
from Characters.playerClasses.oldLady import OldLady
class TestFuriousSlashAttack(TestCase):

    def test_get_damage(self):
        person = OldLady()
        hit = ParasolParry(person.constitution)

        self.assertEqual(5, hit.calcDamage())

