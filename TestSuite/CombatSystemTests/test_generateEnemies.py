import unittest

from CombatSystem.generateEnemies import minCRValue, createEnemyInstances, generateEnemies
from Characters.playerClasses.warlock import Warlock


class TestingGenerateEnemies(unittest.TestCase):

    def test_minCRValueCaluclatesTheMinCrToFillUpSpacesToMaximum4(self):
        TotalCr = 12
        actualMinimumCr = TotalCr//4
        minCrValueOfEnemy = minCRValue(12, 4)
        self.assertGreaterEqual(minCrValueOfEnemy, actualMinimumCr)

    def test_minCRValueCaluclatesTheMinCrToFillUpSpacesToMaximum2(self):
        TotalCr = 5
        actualMinimumCr = TotalCr//2
        minCrValueOfEnemy = minCRValue(12, 4)
        self.assertGreaterEqual(minCrValueOfEnemy, actualMinimumCr)





if __name__ == '__main__':
    unittest.main()
