import pygame
from pygame.locals import *
import time
from Stages.baseStageClass import BaseStage, StageButton
from Stages.Snake2.snakeGame2 import ScoreBox
import random

class MatchScoreBox(ScoreBox): # keeps track of the score and prints it to the screen
    def __init__(self, screen):
        self.score = 0
        print(screen.screen_width)
        self.x = screen.screen_height-50
        self.y = 30
        self.size = 40
        self.scoreBox = Rect((self.x, self.y, self.size, self.size))
        self.font = 'Stages/media/Chapaza.ttf'
        self.color = (255, 255, 255)  # white
        self.display = screen.display
        self.fontSize = 40
        #ToDo: fix scorebox writing on top of old score

class Rock(StageButton):  # Special button for the rocks covering the hidden images
    def __init__(self, screen, num, x, y, underImage, matchID, rockImage):
        buttonText = "Rock"+str(num)
        self.display = screen.display
        super().__init__(buttonText, "", 0, 0)
        self.screen_width = screen.screen_width
        self.screen_height = screen.screen_height
        self.height = 90
        self.width = 90
        self.xLocation, self.yLocation = x, y
        self.rockImage = rockImage
        self.underRockImage = (pygame.image.load("Stages/media/matches/"+underImage).convert_alpha()) # loads the hidden image as a png
        self.image = pygame.transform.scale(self.rockImage, (self.width, self.height))
        self.looking = False
        self.matchID = matchID
        self.Rect = Rect(y, x, self.width, self.height)
        self.active = True

    def displayButton(self, display=None):
        if self.active is True:
            self.display.blit(self.image, (self.xLocation, self.yLocation))

    def lookUnder(self): # shows the image hidden under the rock
        self.image = pygame.transform.scale(self.underRockImage, (self.width, self.height))
        self.displayButton()
        self.looking = True

    def replaceRock(self): # puts the rock back over the image
        self.image = pygame.transform.scale(self.rockImage, (self.width, self.height))
        self.displayButton()
        self.looking = False
        #pygame.display.update(self.Rect)

    def removeRock(self):
        self.active= False

    def __eq__(self, other):
        if self.matchID == other.matchID:
            return True
        return False


class MatchGame(BaseStage):
    def __init__(self, screen):
        self.screen_height = screen.screen_height
        self.screen_width = screen.screen_width
        self.screen = screen

        #Generate prize
        self.prize = self.choosePrize()

        self.score = MatchScoreBox(screen) # keeps track of score and prints to screen
        self.difficulty = 12  # num of matches = difficulty

        # init display screen
        self.display = screen.display
        self.bgImage = pygame.transform.scale(pygame.image.load('Stages/media/trees.png').convert(), (self.screen_height, self.screen_width))

        # Buttons
        self.quitGame = screen.quitGame
        self.okay = StageButton("OK", "", self.screen_height/2 - (self.quitGame.width + 50), self.screen_width/2)
        self.nevermind = StageButton("MAYBE NOT", "", self.screen_height/2 +50, self.screen_width/2)
        hint = "There are toadstools hidden under the rocks\nFind "+str(self.difficulty)+" matching pairs to win"
        self.hint = StageButton("HINT", hint, screen.goBack.xLocation, screen.goBack.yLocation)

        self.activeButtons = [self.quitGame, self.hint]
        self.inactiveButtons = []
        self.selectedButtonName = None

        self.enabled = False  # allows the interactive buttons to be pressed

        self.rockNames = []
        self.rocks = []

        self.closedRocks = [] # rocks that have been matched
        self.choosenRocks = []  # max two flipped rocks at a time
        self.selectedButtonNames = []  # names of selected rocks

        self.hiddenImages = ["ts1.png", "ts2.png", "ts3.png", "ts4.png", "ts5.png", "ts6.png",
                             "ts7.png", "ts8.png", "ts9.png", "ts11.png", "ts12.png",
                             "ts13.png", "ts14.png"]  # potential images to be found under a rock, used to initilize game
        self.rockImage = (pygame.image.load("Stages/media/rockImage.png").convert_alpha()) # loads the rock image as a png, ensure image is only loaded once

        self.finished = False

        self.xyList = []  # to prevent overlap of rocks

    def checkRockLocation(self, x, y):  # detects if rock is generated on top of existing rock: return True if so
        # ToDo: debug
        if [x,y] in self.xyList:
            return True
        return False

    def generateXY(self): # gets a random location on the screen to place a rock
        unsuitable = True
        while unsuitable is True:
            x = (random.randint(1, 12)*100) - 10
            y = (random.randint(2, 6)*100) - 10
            if self.checkRockLocation(x, y) is False:
                self.xyList.append([x,y])
                return x, y
                unsuitable = False

    def getRock(self, name):
        for rock in self.rocks:
            if rock.buttonText == name:
                return rock

    def generateRocks(self):  # generates random positioning of rocks and images underneath.
        matchID = 0
        for num in range(self.difficulty):
            underImage = self.getNewUnderImage()
            for match in range(2):
                x, y = self.generateXY()
                newRock = Rock(self.screen, matchID+match, x, y, underImage, matchID, self.rockImage)
                # print(num, match)
                self.rocks.append(newRock)
                print(newRock.buttonText)
                self.rockNames.append(newRock.buttonText)
                self.activeButtons.append(newRock)
            matchID += 2

    def getNewUnderImage(self):
        num = random.randint(0, len(self.hiddenImages)-1)
        image = self.hiddenImages[num]
        self.hiddenImages.remove(image)
        return image


    def lookUnder(self, rockName): # reveales image under rock
        rock = self.getRock(rockName)
        if rock.looking is False:
            rock.lookUnder()
            self.resetLayers()
            print("pressed:"+str(rock.buttonText))
            self.choosenRocks.append(rock)
            print("len:", len(self.choosenRocks))
            self.selectedButtonNames.append(rock.buttonText)
            if len(self.choosenRocks) == 2:
                self.checkMatching()


    def replaceRocks(self):
        self.choosenRocks[0].replaceRock()
        self.choosenRocks[1].replaceRock()

    def matching(self):
        self.closedRocks += [self.choosenRocks[0].buttonText, self.choosenRocks[1].buttonText]
        self.choosenRocks[0].removeRock()
        self.choosenRocks[1].removeRock()
        self.score.updateScore()
        if self.score.score == self.difficulty:
            return self.gameOver()


    def checkMatching(self):
        self.selectedButtonName = None
        self.selectedButtonNames = []
        if self.choosenRocks[0] == self.choosenRocks[1]:
            print("Match")
            self.matching()
        else:
            print("No match")
            self.replaceRocks()
        self.choosenRocks = []
        time.sleep(0.3)
        if self.finished is not True:
            self.resetLayers()

    def rockLayer(self):
        for rock in self.rocks:
            if rock.buttonText not in self.closedRocks:
                rock.displayButton(self.display)

    def howToPlay(self):
        self.hint.displayWarningMessage(self.display, self.screen_width, self.screen_height)
        self.displayButton(self.okay)
        time.sleep(0.3)
        self.activeButtons = [self.okay]  # deactivates the main menu and treasure box, activates ok option
        return self.hint.buttonText

    def resetLayers(self):
        self.backgroundLayer()
        self.rockLayer()
        self.score.printScore()


    def gameOver(self):  # ends the game when a win/failure occurs
        self.finished = True
        updateRect = Rect((self.screen_height/4, self.screen_width/4, self.screen_height/2, self.screen_width/2))
        pygame.draw.rect(self.display, self.okay.textColor, updateRect)  # border
        pygame.draw.rect(self.display, self.okay.hovercolour, (self.screen_height/4 + 5, self.screen_width/4 + 5,
                                                   self.screen_height/2 - 10, self.screen_width/2 - 10))

        message = "Congrats!\nYou win "+self.prize
        self.activeButtons = [self.okay]
        self.okay.yLocation += 100
        self.okay.displayButton(self.display)
        y = self.screen_width/4 + 50
        for line in message.split('\n'):  # allows for multiple-line output
            font = pygame.font.Font(self.okay.font, 40)
            text = font.render(line, True, (self.okay.textColor))
            textRect = text.get_rect()
            textRect.center = (self.screen_height/2, y)
            y += 50
            self.display.blit(text, textRect)
            self.selectedButtonName = "ENDGAME"
        pygame.display.update()


    def mouseClick(self, button):  # event handler for button press
        if button.buttonText in ["QUIT", "SKIP", "BACK"]:
            self.selectedButtonName = self.warningMessage(button)
        elif button.buttonText in self.rockNames:
            if button.buttonText not in (self.selectedButtonNames and self.closedRocks):
                #self.selectedButtonName = button.buttonText  # ToDo: recheck this
                self.lookUnder(button.buttonText)
        elif button.buttonText == "OK":
            if self.selectedButtonName in ["QUIT", "ENDGAME"]:
                self.exitGame()
            elif self.selectedButtonName in ["HINT"]:
                self.maybeNot()
        elif button.buttonText == "MAYBE NOT":
            self.maybeNot()
        elif button.buttonText == "HINT":
            self.selectedButtonName = button.buttonText
            self.howToPlay()

    def maybeNot(self):
        self.selectedButtonName = None
        self.enabled = False
        self.activeButtons = [self.quitGame, self.hint] + self.rocks
        self.backgroundLayer()
        self.rockLayer()

    def choosePrize(self):
        # Todo: choose an attribute to increase, increase it, return prize name as string, chosen at random?
        return "nothing"


    def mainLoop(self):  # listens for events
        self.generateRocks()
        self.resetLayers()

        mainLoop = True

        while mainLoop:
            if self.enabled:
                self.listenMouse()
                self.listenButton()
            else:
                time.sleep(0.3)  # Delay before reactivating the treasure, to prevent accidental opening of chest
                self.enabled = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainLoop = False

"""# Can be uncommented For testing purposes but must be commented to stop overriding of main:
pygame.init()
s = BaseStage(1300, 700)
baseStage = MatchGame(s)
baseStage.mainLoop()
pygame.quit()"""
