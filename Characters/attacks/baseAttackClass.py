import pygame

class BaseAttack(object):
    def __init__(self):
        self.name = 'Base'
        self.baseDamage = 0
        self.description = 'base class discription'
        self.damageMod = 0
        self.coolDown = 0
        self.duration = 0


    def getDamage(self):
        damage = self.baseDamage + ((self.damageMod - 10) // 2)
        return damage

    def playAttackSound(self, attackAudioFilePath):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(attackAudioFilePath)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

