import pygame

from Characters.sharedFunctions import calc_attribute_bonus


class BaseAttack():
    def __init__(self):
        self.name = 'Base'
        self.baseDamage = 0
        self.description = 'base class description'
        self.damageMod = 0
        self.coolDown = 0
        self.duration = 0
        self.name = "Temp"
        self.onCoolDown = False
        self.isHeal = False
        self.isAOE = False
        self.healType = "none"
        self.coolDownTimer = 0

    def startCooldown(self):
        self.coolDownTimer = self.coolDown
        self.onCoolDown = True

    def reduceCoolDown(self):
        self.coolDownTimer -= 1
        if self.coolDownTimer <= 0:
            self.onCoolDown = False

    def resetCoolDown(self):
        self.coolDownTimer = 0
        self.onCoolDown = False

    def calcDamage(self):
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

