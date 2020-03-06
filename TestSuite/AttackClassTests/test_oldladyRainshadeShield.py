from unittest import TestCase
from Characters.attacks.playableCharacterAttacks.oldLady.RainshadeShield import GlorPres
from Characters.playerClasses.oldLady import OldLady
class TestFuriousSlashAttack(TestCase):

    def test_get_damage(self):
        person = OldLady()
        hit = GlorPres(person.constitution)

        self.assertEqual(23, hit.calcDamage())

