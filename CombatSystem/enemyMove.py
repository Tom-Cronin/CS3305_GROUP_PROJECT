def getPlayerToAttack(listOfPlayers):
    player_with_max_health = listOfPlayers[0]
    playerMaxHealth = 0
    playerLeastHealth = 9999
    player_with_least_health = listOfPlayers[0]
    for player in listOfPlayers:
        if player.health > playerMaxHealth:
            player_with_max_health = player
            playerMaxHealth = player.health
        if player.health < playerLeastHealth:
            player_with_least_health = player
            playerLeastHealth = player.health
    return player_with_least_health, player_with_max_health, playerLeastHealth, playerMaxHealth

def getMaxDamageAttack(enemy):
    count = 0
    maxDamage = 0
    myAttack = 0
    attacks = enemy.allAttacks[0]
    for attack in enemy.allAttacks:

        if not attack.onCoolDown and attack.getDamage() > maxDamage:
            attacks = attack
            myAttack = count
            maxDamage = attack.getDamage()
            count += 1
    return myAttack, maxDamage

def makeMove(enemy, listOfPlayers):
    if len(listOfPlayers) > 0:
        player_with_least_health, player_with_max_health, playerLeastHealth, playerMaxHealth = getPlayerToAttack(
            listOfPlayers)
        myAttack, maxDamage = getMaxDamageAttack(enemy)
        enemy.allAttacks[myAttack].startCooldown()

        if maxDamage >= playerLeastHealth:
            return maxDamage, player_with_least_health

        return [maxDamage, player_with_max_health]
    return [0, enemy]
