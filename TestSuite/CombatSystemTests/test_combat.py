import unittest

from CombatSystem.combat import combatEncounter
from Characters.playerClasses.warlock import Warlock


class TestingCombat(unittest.TestCase):

    def test_setUpCorrectlySetsUpAllAttributes(self):
        myCombat = combatEncounter()
        myWarlock = Warlock()
        self.assertEqual(myCombat.enemies, [])
        self.assertEqual(myCombat.allies, [])
        self.assertEqual(myCombat.turnOrder, [])
        self.assertEqual(myCombat.allCharsInFight, [])
        myCombat.setUp(12, [myWarlock])
        self.assertEqual(len(myCombat.enemies), 4)
        self.assertEqual(len(myCombat.turnOrder), 5)
        self.assertEqual(len(myCombat.allCharsInFight), 5)
        self.assertEqual(myCombat.allies, [myWarlock])
        
    def test_calcDamagesReducesCharacterHealth(self):
        myCombat = combatEncounter()
        warlockTakingDamage = Warlock()
        baseHealth = warlockTakingDamage.health
        didItDie = myCombat.calcDamage([1, warlockTakingDamage])
        self.assertFalse(didItDie)
        self.assertEqual(warlockTakingDamage.health, (baseHealth -1))

    def test_calcDamagesReturnsCharacterDeath(self):
        myCombat = combatEncounter()
        warlockTakingDamage = Warlock()
        myCombat.setUp(12, [warlockTakingDamage])
        didItDie = myCombat.calcDamage([999, warlockTakingDamage])
        self.assertTrue(didItDie)



if __name__ == '__main__':
    unittest.main()
