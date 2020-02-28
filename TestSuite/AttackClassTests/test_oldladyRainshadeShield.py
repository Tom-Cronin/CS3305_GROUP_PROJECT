from unittest import TestCase
from Characters.attacks.playableCharacterAttacks.oldLady.RainshadeShield import RainshadeShield
from Characters.playerClasses.oldLady import OldLady
class TestFuriousSlashAttack(TestCase):

    def test_get_damage(self):
        person = OldLady()
        hit = RainshadeShield(person.constitution)

        self.assertEqual(3, hit.calcDamage())

