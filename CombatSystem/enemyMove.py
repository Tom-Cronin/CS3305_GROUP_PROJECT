
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
    return playerWithLeastHealth, playerWithMaxHealth, playerLeastHealth, playerMaxHealth

def getMaxDamageAttack(enemy):
    count = 0
    maxDamage = 0
    myAttack = 0
    for attack in enemy.allAttacks:
        if not attack.onCoolDown and attack.getDamage() > maxDamage:
            myAttack = count
            maxDamage = attack.getDamage()
        count += 1
    return myAttack, maxDamage

def makeMove(enemy, listOfPlayers):
    if len(listOfPlayers) > 0:
        playerWithLeastHealth, playerWithMaxHealth, playerLeastHealth, playerMaxHealth = getPlayersToAttack(
            listOfPlayers)
        myAttack, maxDamage = getMaxDamageAttack(enemy)
        enemy.allAttacks[myAttack].startCooldown()
        if maxDamage >= playerLeastHealth:
            return [maxDamage, playerWithLeastHealth]
        return [maxDamage, playerWithMaxHealth]
    return [0, enemy]
