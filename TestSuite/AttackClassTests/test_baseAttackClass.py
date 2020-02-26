from unittest import TestCase
from Characters.attacks.baseAttackClass import BaseAttack

class TestBaseAttack(TestCase):

    def test_get_damage(self):
        attack = BaseAttack()
        self.assertEqual(0, attack.calcDamage())


    def test_update_damage_mod(self):
        attack = BaseAttack()
        self.assertEqual(attack.damageMod, 0)
        attack.updateDamageMod(20)
        self.assertEqual(5, attack.damageMod)

#x - 10 /2
