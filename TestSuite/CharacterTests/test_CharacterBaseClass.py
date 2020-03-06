from unittest import TestCase
from Characters.BaseClass.CharacterBaseClass import Character


class TestCharacter(TestCase):

    def test_healthShouldUpdateWithNegativeConstitutionBonus(self):
        self.char = Character()
        self.assertEqual(self.char.health, 0)
        self.char.setHealth(10)
        self.assertEqual(5, self.char.health)

    def test_healthShouldUpdateWithNoConstitutionBonus(self):
        self.char = Character()
        self.assertEqual(self.char.health, 0)
        self.char.constitution = 10
        self.char.setHealth(10)
        self.assertEqual(10, self.char.health)

    def test_healthShouldUpdateWithConstitutionBonus(self):
        self.char = Character()
        self.assertEqual(self.char.health, 0)
        self.char.constitution = 20
        self.char.setHealth(10)
        self.assertEqual(15, self.char.health)

    def test_levelUpShouldIncreaseSelectedAttribute(self):
        self.char = Character()
        self.assertEqual(0, self.char.intelligence)
        self.char.levelUp("intelligence", 1)
        self.assertEqual(1, self.char.intelligence)


    def test_characterShouldTakeDamage(self):
        self.char = Character()
        self.char.health = 20
        self.assertEqual(20, self.char.health)
        self.char.takeDamage(5)
        self.assertEqual(15, self.char.health)

    def test_shouldRollInitiativeWithAValueOfDexModOrHigher(self):
        self.char = Character()
        self.char.dexterity = 410
        self.assertGreaterEqual(self.char.rollInitative(), 200)