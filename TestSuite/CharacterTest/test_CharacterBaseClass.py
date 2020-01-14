from unittest import TestCase
from Characters.BaseClass import CharacterBaseClass


class TestCharacter(TestCase):

    @classmethod
    def tearDown(self):
        self.char = None

    def test_getHealth(self):
        self.char = CharacterBaseClass.Character()
        self.assertEqual(self.char.getHealth(), 0)

    def test_getConstitution(self):
        self.char = CharacterBaseClass.Character()
        self.assertEqual(self.char.getConstitution(), 0)

    def test_getDex(self):
        self.char = CharacterBaseClass.Character()
        self.assertEqual(self.char.getDex(), 0)

    def test_getStr(self):
        self.char = CharacterBaseClass.Character()
        self.assertEqual(self.char.getStrenght(), 0)

    def test_getInt(self):
        self.char = CharacterBaseClass.Character()
        self.assertEqual(self.char.getInt(), 0)

    def test_getInit(self):
        self.char = CharacterBaseClass.Character()
        self.assertEqual(self.char.getInitative(), 0)

    def test_getAC(self):
        self.char = CharacterBaseClass.Character()
        self.assertEqual(self.char.getAC(), 0)


    def test_healthShouldUpdateWithNoConstitutionBonus(self):
        self.char = CharacterBaseClass.Character()
        self.assertEqual(self.char.getHealth(), 0)
        self.char.setHealth(10)
        self.assertEqual(self.char.getHealth(), 10)


    def test_healthShouldUpdateWithConstitutionBonus(self):
        self.char = CharacterBaseClass.Character()
        self.char.setConstitution(10)
        self.assertEqual(self.char.getHealth(), 0)
        self.char.setHealth(10)
        self.assertEqual(self.char.getHealth(), 20)

