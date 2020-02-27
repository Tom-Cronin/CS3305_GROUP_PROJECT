
def turnOrder(combatList):
    turnOrderStack = []
    thidict = {}

    for charcater in combatList:
        rollinit = charcater.rollInitative()
        thidict[charcater] = rollinit
    sortDict = {k: v for k, v in sorted(thidict.items(), reverse=True, key=lambda item: item[1] )}

    name_list = []
    for character in sortDict:

        turnOrderStack.append(character)
        if character.isEnemy:
            counter = name_list.count(character.name) + 1
            name_list.append(character.name)
            character.name = character.name + " " + str(counter)

    return turnOrderStack












