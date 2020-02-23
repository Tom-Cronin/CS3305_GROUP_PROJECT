import unittest

from CombatSystem.enemyMove import getMaxDamageAttack, getPlayersToAttack, makeMove
from Characters.playerClasses.warlock import Warlock


class TestEnemyMove(unittest.TestCase):

    def test_getMaxDamageCorrectlyGetsTheHighestAttackDamage(self):
        myEnemy = Warlock()
        attackBeingChanged = 1

        myEnemy.attack_slot_1.damageMod = 0
        myEnemy.attack_slot_2.damageMod = 10
        myEnemy.attack_slot_3.damageMod = 0
        myEnemy.attack_slot_4.damageMod = 0

        myEnemy.attack_slot_1.baseDamage = 0
        myEnemy.attack_slot_2.baseDamage = 10
        myEnemy.attack_slot_3.baseDamage = 0
        myEnemy.attack_slot_4.baseDamage = 0

        ChosenAttack, AttackDamage = getMaxDamageAttack(myEnemy)

        self.assertEqual(ChosenAttack, attackBeingChanged)
        self.assertEqual(myEnemy.allAttacks[ChosenAttack], myEnemy.attack_slot_2)
        self.assertEqual(AttackDamage, 20)

    def test_getMaxDamageReturnsTheFirstAttackIfAllTheAttacksHaveSameDamage(self):
        myEnemy = Warlock()

        myEnemy.attack_slot_1.damageMod = 0
        myEnemy.attack_slot_2.damageMod = 0
        myEnemy.attack_slot_3.damageMod = 0
        myEnemy.attack_slot_4.damageMod = 0

        myEnemy.attack_slot_1.baseDamage = 0
        myEnemy.attack_slot_2.baseDamage = 0
        myEnemy.attack_slot_3.baseDamage = 0
        myEnemy.attack_slot_4.baseDamage = 0

        ChosenAttack, AttackDamage = getMaxDamageAttack(myEnemy)

        self.assertEqual(ChosenAttack, 0)
        self.assertEqual(myEnemy.allAttacks[ChosenAttack], myEnemy.attack_slot_1)
        self.assertEqual(AttackDamage, 0)

    def test_getPlayersToAttackShouldReturnTheFirstPlayerInListIfAllHealthsAreTheSame(self):
        firstWarlock = Warlock()
        secondWarlock = Warlock()
        thirdWarlock = Warlock()
        fourthWarlock = Warlock()
        firstWarlock.health = 10
        secondWarlock.health = 10
        thirdWarlock.health = 10
        fourthWarlock.health = 10

        playerList = [firstWarlock,secondWarlock,thirdWarlock,fourthWarlock]
        playerWithLeastHealth, playerWithMaxHealth, playerLeastHealth, playerMaxHealth = getPlayersToAttack(playerList)
        self.assertEqual(firstWarlock, playerWithLeastHealth)
        self.assertEqual(firstWarlock, playerWithMaxHealth)

    def test_getPlayersToAttackShouldReturnThePlayersWithTheLowestAndHighestHealth(self):
        MaxHPWarlock = Warlock()
        MaxHPWarlock.health = 130
        MinHPWarlock = Warlock()
        MinHPWarlock.health = 1
        Warlock1= Warlock()
        Warlock1.health = 10
        Warlock2 = Warlock()
        Warlock2.health = 10

        playerList = [Warlock1,MaxHPWarlock,MinHPWarlock,Warlock2]
        playerWithLeastHealth, playerWithMaxHealth, playerLeastHealth, playerMaxHealth = getPlayersToAttack(playerList)
        self.assertEqual(MinHPWarlock, playerWithLeastHealth)
        self.assertEqual(MaxHPWarlock, playerWithMaxHealth)
        self.assertEqual(MaxHPWarlock.health, playerMaxHealth)
        self.assertEqual(MinHPWarlock.health, playerLeastHealth)

    def test_makeMoveShouldPrioritiseKillingAPlayerOverDamagingOtherPlayers(self):
        MaxHPWarlock = Warlock()
        MaxHPWarlock.health = 130
        MinHPWarlock = Warlock()
        MinHPWarlock.health = 1
        Warlock1 = Warlock()
        Warlock1.health = 10
        Warlock2 = Warlock()
        Warlock2.health = 10

        myEnemy = Warlock()

        playerList = [Warlock1, MaxHPWarlock, MinHPWarlock, Warlock2]
        damage, PlayerToHit = makeMove(myEnemy, playerList)
        self.assertEqual(PlayerToHit, MinHPWarlock)
        self.assertTrue(damage >= 1)

    def test_makeMoveShouldPrioritiseDamagingTheHighestHealthPlayerIfItCantKillAPlayer(self):
        MaxHPWarlock = Warlock()
        MaxHPWarlock.health = 130
        MinHPWarlock = Warlock()
        MinHPWarlock.health = 70
        Warlock1 = Warlock()
        Warlock1.health = 80
        Warlock2 = Warlock()
        Warlock2.health = 80

        myEnemy = Warlock()

        playerList = [Warlock1, MaxHPWarlock, MinHPWarlock, Warlock2]
        damage, PlayerToHit = makeMove(myEnemy, playerList)
        self.assertEqual(PlayerToHit, MaxHPWarlock)


if __name__ == '__main__':
    unittest.main()
