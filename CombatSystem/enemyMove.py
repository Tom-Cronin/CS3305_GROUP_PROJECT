import time

def makeMove(enemy, listOfPlayers):
    if len(listOfPlayers) > 0:
        player_with_max_health = listOfPlayers[0]
        playerMaxHealth = 0
        playerLeastHealth = 9999
        player_with_least_health = listOfPlayers[0]
        maxDamage = 0
        myAttack = 0

        for player in listOfPlayers:
            if player.health > playerMaxHealth:
                player_with_max_health = player
                playerMaxHealth = player.health
            if player.health < playerLeastHealth:
                player_with_least_health = player
                playerLeastHealth = player.health
        count = 0
        for attack in enemy.allAttacks:
            if not attack.onCoolDown and attack.getDamage() > maxDamage:
                myAttack = count
                maxDamage = attack.getDamage()
                count += 1
        enemy.allAttacks[myAttack].startCooldown()
        if maxDamage >= playerLeastHealth:
            return maxDamage, player_with_least_health

        return [maxDamage, player_with_max_health]
    return [0, enemy]
