
from Stages.baseStageClass import *
import time
from textInput import  TextInput



class HealStage():

    def __init__(self, screen,team):
        self.team = team
        self.font = 'Stages/media/Chapaza.ttf'
        self.fontsize = 20
        self.baseScreen = screen
        self.baseScreen.bgImage = pygame.transform.scale(pygame.image.load('Stages/media/MainMenueBackground.png').convert(),
                                                         (self.baseScreen.screen_height, self.baseScreen.screen_width))


    def display(self):
        self.baseScreen.display.blit(self.baseScreen.bgImage, (0, 0))
        font = pygame.font.Font(self.font, self.fontsize)
        name = font.render("You take time to rest and recover", True, (0,0,0))
        text = font.render("Everyone heals fully", True, (0,0,0))

        pygame.draw.rect(self.baseScreen.display, (0, 0, 0), (445, 52, 400, 75))
        pygame.draw.rect(self.baseScreen.display, (255, 255, 255), (450, 57, 390, 65))
        self.baseScreen.display.blit(name, (490, 68))
        self.baseScreen.display.blit(text, (540, 98))

        pygame.display.update()

    def restoreHealth(self):
        for ally in self.team:
            ally.health = ally.maxHealth
        return False


    def mainLoop(self):  # listens for events
        self.display()
        mainLoop = True
        while (mainLoop):
            mainLoop = self.restoreHealth()
            time.sleep(3)

if __name__=="__main__":
        baseScreen = BaseStage(1300, 700)
        pygame.init()
        pygame.mixer.init()
        myStage =HealStage(baseScreen, [])
        myStage.mainLoop()
        pygame.quit()
