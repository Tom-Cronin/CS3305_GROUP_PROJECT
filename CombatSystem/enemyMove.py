from time import sleep

def getPlayersToAttack(listOfPlayers):
    playerWithMaxHealth = listOfPlayers[0]
    playerMaxHealth = 0
    playerLeastHealth = 9999
    playerWithLeastHealth = listOfPlayers[0]

    for player in listOfPlayers:
        if player.health > playerMaxHealth:
            playerWithMaxHealth = player
            playerMaxHealth = player.health
        if player.health < playerLeastHealth:
            playerWithLeastHealth = player
            playerLeastHealth = player.health
    return playerWithLeastHealth, playerWithMaxHealth

def getMaxDamageAttack(enemy,playerLength):

    count = 0
    maxDamage = 0
    myAttack = 0
    for attack in enemy.allAttacks:
        if not attack.onCoolDown:
            if attack.isAOE:
                test = attack.calcDamage()
                test *= playerLength
                if test > maxDamage:
                    myAttack = count
                    maxDamage = test
            else:
                if attack.calcDamage() > maxDamage:
                    myAttack = count
                    maxDamage = attack.calcDamage()
        count += 1
    return myAttack, maxDamage

def makeMove(enemy, listOfPlayers):
    sleep(1)
    if len(listOfPlayers) > 0:
        playerWithLeastHealth, playerWithMaxHealth = getPlayersToAttack(listOfPlayers)
        myAttackIndex, maxDamage = getMaxDamageAttack(enemy, len(listOfPlayers))
        enemy.allAttacks[myAttackIndex].startCooldown()
        if enemy.allAttacks[myAttackIndex].isAOE:
            return [enemy.allAttacks[myAttackIndex], "all"]
        if maxDamage >= playerWithLeastHealth.health:
            return [enemy.allAttacks[myAttackIndex], playerWithLeastHealth]
        return [enemy.allAttacks[myAttackIndex], playerWithMaxHealth]

    return [0, enemy]
