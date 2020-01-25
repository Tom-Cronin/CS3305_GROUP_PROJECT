import pygame, sys
from pygame.locals import *
from Stages.baseStageClass import BaseStage
pygame.init()
baseStage = BaseStage()
baseStage.mainLoop(800, 600)
pygame.quit()