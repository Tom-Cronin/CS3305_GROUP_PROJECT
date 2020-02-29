from Characters.enemyClasses import Hag, Rat, ShadowJest, Shadowling, GateGuard

CR_MAX_VALUE = 3
CR_MIN_VALUE = 1

# dictionaryOfMonsters = {
#     1: [Rat.Rat],
#     2: [Rat.Rat],
#     3: [Hag.Hag]
# }

dictionaryOfMonsters = {
    1: [Shadowling.Shadowling, Rat.Rat],
    2: [ShadowJest.ShadowJest],
    3: [Hag.Hag]
}
dictionaryOfBoss = {
    1: [GateGuard.GateGuard]
}

