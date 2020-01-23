
class BaseAttack(object):
    def __init__(self):
        self.name = 'Base'
        self.baseDamage = 0
        self.description = 'base class discription'
        self.damageMod = 0


    def getDamage(self):
        damage = self.baseDamage + ((self.damageMod - 10) // 2)
        print("function ",  self.baseDamage)
        print("modded damage ", ((self.damageMod - 10) // 2))
        return damage


