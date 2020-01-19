from unittest import TestCase
from Characters.BaseClass.CharacterBaseClass import Character


class TestCharacter(TestCase):

    @classmethod
    def tearDown(self):
        self.char = None

    def test_getHealth(self):
        self.char = Character()
        self.assertEqual(self.char.getHealth(), 0)

    def test_getConstitution(self):
        self.char = Character()
        self.assertEqual(self.char.getConstitution(), 0)

    def test_setConstitution(self):
        self.char = Character()
        self.assertEqual(self.char.getConstitution(), 0)
        self.char.setConstitution(10)
        self.assertEqual(self.char.getConstitution(), 10)

    def test_getDex(self):
        self.char = Character()
        self.assertEqual(self.char.getDex(), 0)

    def test_setDex(self):
        self.char = Character()
        self.assertEqual(self.char.getDex(), 0)
        self.char.setDex(10)
        self.assertEqual(self.char.getDex(), 10)

    def test_getStr(self):
        self.char = Character()
        self.assertEqual(self.char.getStrenght(), 0)

    def test_setStr(self):
        self.char = Character()
        self.assertEqual(self.char.getStrenght(), 0)
        self.char.setStrength(10)
        self.assertEqual(self.char.getStrenght(), 10)

    def test_getInt(self):
        self.char = Character()
        self.assertEqual(self.char.getInt(), 0)

    def test_setInt(self):
        self.char = Character()
        self.assertEqual(self.char.getInt(), 0)
        self.char.setInt(10)
        self.assertEqual(self.char.getInt(), 10)

    def test_getInit(self):
        self.char = Character()
        self.assertEqual(self.char.getInitative(), 0)

    def test_setInit(self):
        self.char = Character()
        self.assertEqual(self.char.getInitative(), 0)
        self.char.setInitiative(10)
        self.assertEqual(self.char.getInitative(), 10)

    def test_getAC(self):
        self.char = Character()
        self.assertEqual(self.char.getAC(), 0)

    def test_setAC(self):
        self.char = Character()
        self.assertEqual(self.char.getAC(), 0)
        self.char.setAC(10)
        self.assertEqual(self.char.getAC(), 10)

    def test_healthShouldUpdateWithNoConstitutionBonus(self):
        self.char = Character()
        self.assertEqual(self.char.getHealth(), 0)
        self.char.setHealth(10)
        self.assertEqual(self.char.getHealth(), 10)

    def test_healthShouldUpdateWithConstitutionBonus(self):
        self.char = Character()
        self.char.setConstitution(10)
        self.assertEqual(self.char.getHealth(), 0)
        self.char.setHealth(10)
        self.assertEqual(self.char.getHealth(), 20)