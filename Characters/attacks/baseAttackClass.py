import pygame

from Characters.sharedFunctions import calc_attribute_bonus


class BaseAttack(object):
    def __init__(self):
        self.name = 'Base'
        self.baseDamage = 0
        self.description = 'base class discription'
        self.damageMod = 0
        self.coolDown = 0
        self.duration = 0

    def getDamage(self):
        return self.baseDamage + self.damageMod

    def updateDamageMod(self, newDamageModAttribute):
        self.damageMod = calc_attribute_bonus(newDamageModAttribute)

    def playAttackSound(self, attackAudioFilePath):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(attackAudioFilePath)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

