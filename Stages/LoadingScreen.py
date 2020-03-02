from Stages.baseStageClass import *
import time

class LoadingScreen:
    def __init__(self, screen):
        self.baseScreen = screen

    def backgroundLayer(self):
        self.baseScreen.display.blit(self.baseScreen.bgImage, (0, 0))

        # Draw white background padding for loading bar.
        pygame.draw.rect(self.baseScreen.display, (255, 255, 255), (167, 560, self.baseScreen.screen_height - 334, 30))
        pygame.draw.rect(self.baseScreen.display, (255, 255, 255), (185, 542, self.baseScreen.screen_height - 370, 66))
        pygame.draw.circle(self.baseScreen.display, (255, 255, 255), (185, 560), 18)
        pygame.draw.circle(self.baseScreen.display, (255, 255, 255), (self.baseScreen.screen_height - 185, 560), 18)
        pygame.draw.circle(self.baseScreen.display, (255, 255, 255), (185, 590), 18)
        pygame.draw.circle(self.baseScreen.display, (255, 255, 255), (self.baseScreen.screen_height - 185, 590), 18)

        # Draw grey background for loading bar.
        pygame.draw.rect(self.baseScreen.display, (120, 120, 120), (175, 560, self.baseScreen.screen_height - 350, 30))
        pygame.draw.rect(self.baseScreen.display, (120, 120, 120), (185, 550, self.baseScreen.screen_height - 370, 50))
        pygame.draw.circle(self.baseScreen.display, (120, 120, 120), (185, 560), 10)
        pygame.draw.circle(self.baseScreen.display, (120, 120, 120), (self.baseScreen.screen_height - 185, 560), 10)
        pygame.draw.circle(self.baseScreen.display, (120, 120, 120), (185, 590), 10)
        pygame.draw.circle(self.baseScreen.display, (120, 120, 120), (self.baseScreen.screen_height - 185, 590), 10)
        pygame.display.update()

    def mainloop(self):
        self.backgroundLayer()
        i = 0
        barLength = (self.baseScreen.screen_height - 350) / 200
        barJump = 199
        while i <= 199:
            pygame.draw.rect(self.baseScreen.display, (0, 191, 255), (175, 570, (self.baseScreen.screen_height - 350) - (barLength * barJump), 10))
            pygame.display.update()
            i += 1
            barJump -= 1
            time.sleep(0.01)
