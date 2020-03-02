from Stages.baseStageClass import *
import time

class LoadingScreen:
    def __init__(self, screen):
        self.baseScreen = screen

    def backgroundLayer(self):

        # Draw white background padding for loading bar.
        pygame.draw.rect(self.baseScreen.display, (255, 255, 255), (292, 560, self.baseScreen.screen_height - 584, 30))
        pygame.draw.rect(self.baseScreen.display, (255, 255, 255), (310, 542, self.baseScreen.screen_height - 620, 66))
        pygame.draw.circle(self.baseScreen.display, (255, 255, 255), (310, 560), 18)
        pygame.draw.circle(self.baseScreen.display, (255, 255, 255), (self.baseScreen.screen_height - 310, 560), 18)
        pygame.draw.circle(self.baseScreen.display, (255, 255, 255), (310, 590), 18)
        pygame.draw.circle(self.baseScreen.display, (255, 255, 255), (self.baseScreen.screen_height - 310, 590), 18)

        # Draw grey background for loading bar.
        pygame.draw.rect(self.baseScreen.display, (120, 120, 120), (300, 560, self.baseScreen.screen_height - 600, 30))
        pygame.draw.rect(self.baseScreen.display, (120, 120, 120), (310, 550, self.baseScreen.screen_height - 620, 50))
        pygame.draw.circle(self.baseScreen.display, (120, 120, 120), (310, 560), 10)
        pygame.draw.circle(self.baseScreen.display, (120, 120, 120), (self.baseScreen.screen_height - 310, 560), 10)
        pygame.draw.circle(self.baseScreen.display, (120, 120, 120), (310, 590), 10)
        pygame.draw.circle(self.baseScreen.display, (120, 120, 120), (self.baseScreen.screen_height - 310, 590), 10)
        pygame.display.update()

    def mainloop(self):
        self.backgroundLayer()
        i = 0
        bar_length = (self.baseScreen.screen_height - 600) / 200
        bar_jump = 199
        while i <= 199:
            pygame.draw.rect(self.baseScreen.display, (0, 191, 255), (300, 570, (self.baseScreen.screen_height - 600) - (bar_length * bar_jump), 10))
            pygame.display.update()
            i += 1
            bar_jump -= 1
            time.sleep(0.01)
