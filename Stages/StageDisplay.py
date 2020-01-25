import pygame, sys
from pygame.locals import *
from Stages.baseStageClass import BaseStage
pygame.init()
baseStage = BaseStage(800, 600)
baseStage.mainLoop()
pygame.quit()