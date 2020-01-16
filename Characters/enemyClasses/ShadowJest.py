from Characters.BaseClass.CharacterBaseClass import Character

class ShadowJest(Character):

    def __init__(self):
        super().__init__()
        self.setStrength(16)
        self.setDex(14)
        self.setConstitution(13)
        self.setInt(5)
        self.setInitiative(2)

        self.setHealth(33)

