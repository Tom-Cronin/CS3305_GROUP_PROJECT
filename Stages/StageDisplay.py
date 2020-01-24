import pygame, sys
from pygame.locals import *
from Stages.baseStageClass import BaseStage

pygame.init()

baseStage = BaseStage()

#Create a displace surface object
StageDisplay = pygame.display.set_mode((800, 600))
#StageDisplay.fill(BaseStage.bgColour)
StageDisplay.blit(pygame.image.load(BaseStage.bgImage), (0, 0))


mainLoop = True

baseStage.displayButton(StageDisplay, baseStage.quitGame)
baseStage.displayButton(StageDisplay, baseStage.goBack)
baseStage.displayButton(StageDisplay, baseStage.skip)

while mainLoop:
    baseStage.listen(StageDisplay)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False

    pygame.display.update()


pygame.quit()