import pygame, sys
from pygame.locals import *

class StageButton:
    def __init__(self, text, exitMessage, x, y):
        self.buttonText = text
        # Note: all three colors below must be different for warningMessage() and hover() to work
        self.defaultColour = (255, 255, 255)  # white
        self.textColor = (0, 255, 0)  # green
        self.hovercolour = (0, 0, 0)  # black

        self.bgColour = self.defaultColour
        self.width = 200
        self.height = 50
        self.xLocation = x
        self.yLocation = y
        self.font = 'Stages/media/Chapaza.ttf'
        self.fontsize = 30
        self.exitMessage = exitMessage  # Message displayed when button is pressed
        self.hovering = False
        # self.buttonImage = pygame.transform.scale(pygame.image.load(buttonImage).convert(),
        #                                               (self.height, self.width))


    def displayButton(self, display):
        pygame.draw.rect(display, self.textColor, (self.xLocation, self.yLocation, self.width, self.height))  # border
        pygame.draw.rect(display, self.bgColour, (self.xLocation+5, self.yLocation+5, self.width-10, self.height-10))
        text = self.buttonText
        font = pygame.font.Font(self.font, self.fontsize)
        text = font.render(text, True, self.textColor)
        textRect = text.get_rect()
        textRect.center = ((self.xLocation+(self.width/2)), self.yLocation+(self.height/2))
        display.blit(text, textRect)

    def displayWarningMessage(self, display, height, width):
        updateRect = Rect((width/4, height/4, width/2, height/2))
        pygame.draw.rect(display, self.textColor, updateRect)  # border
        pygame.draw.rect(display, self.bgColour, ((width/4)+5, (height/4)+5, (width/2)-10, (height/2)-10))
        y = (height/4 + 50)
        for line in self.exitMessage.split('\n'):  # allows for multiple-line output
            font = pygame.font.Font(self.font, 20)
            text = font.render(line, True, self.textColor)
            textRect = text.get_rect()
            textRect.center = ((width/2), y)
            y += 50
            display.blit(text, textRect)
        pygame.display.update(updateRect)

    def hover(self, display, hover):
        self.hovering = hover
        if hover is True:
            self.bgColour = self.hovercolour
            self.displayButton(display)
        else:
            self.bgColour = self.defaultColour
            self.displayButton(display)


class DisabledStageButton(StageButton):

    def __init__(self, text, exitMessage, x, y):
        super().__init__(text, exitMessage, x, y)

        self.bgColour = (100, 100, 100)
        self.textColor = (255, 255, 255)
        self.textColorDisabled = (0, 0, 0)
        self.disabledMessage = "You cannot "+self.buttonText+" at this stage"  # Message displayed when button is pressed
        self.disabledMessageSize = 12

    def hover(self, display, hover):
        self.hovering = hover
        messageRect = Rect(self.xLocation, self.yLocation+self.height, self.width, self.height/2)
        if hover is True:
            pygame.draw.rect(display, self.textColor, messageRect)  # border
            message = self.disabledMessage
            font = pygame.font.Font(self.font, self.disabledMessageSize)
            text = font.render(message, True, self.textColorDisabled)
            textRect = text.get_rect()
            textRect.center = ((self.xLocation + (self.width / 2)), self.yLocation+self.height +self.height/4)
            display.blit(text, textRect)

        if hover is False:
            self.displayButton(display)

        pygame.display.update(messageRect)


class BaseStage:

    def __init__(self, screen_height, screen_width):
        # init display screen
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.display = pygame.display.set_mode((screen_height, screen_width))

        # Buttons
        self.quitGame = StageButton("QUIT", "Are you sure you want to quit the game?\nYour data will not be saved", 10, 10)
        self.goBack = StageButton("BACK", "Are you sure you want to leave?\nYour data will not be saved", 300, 10)
        self.skip = StageButton("SKIP", "Are you sure you want to skip?\nYou will not gain any rewards from this stage", 590, 10)
        self.okay = StageButton("OK", "", self.screen_height / 2 - (self.quitGame.width + 50), self.screen_width / 2)
        self.nevermind = StageButton("MAYBE NOT", "", self.screen_height / 2 + 50, self.screen_width / 2)

        self.activeButtons = [self.quitGame, self.goBack, self.skip]
        self.inactiveButtons = []  # buttons that are visible but deactivated
        self.selectedButtonName = None

        self.bgImage = pygame.transform.scale(pygame.image.load('Stages/media/trees.png').convert(), (self.screen_height, self.screen_width))
    
    def displayButton(self, button):
        button.displayButton(self.display)

    def warningMessage(self, button):
        # Warning message is displayed when the player attempts to leave the stage
        button.displayWarningMessage(self.display, self.screen_width, self.screen_height)
        self.displayButton(self.okay)
        self.displayButton(self.nevermind)
        self.activeButtons = [self.okay, self.nevermind]  # deactivates the main menu, activates ok and nm options
        return button.buttonText

    def listenMouse(self):  # listens for hovering/clicking of mouse
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for button in self.activeButtons+self.inactiveButtons:
            if (button.xLocation + button.width) > mouse[0] > button.xLocation and (
                    button.yLocation + button.height) > mouse[1] > button.yLocation:
                button.hover(self.display, True)
                if button not in self.inactiveButtons:
                    if click[0] == 1:
                        self.mouseClick(button)
            else:
                if button.hovering is True:
                    button.hover(self.display, False)
                    if button in self.inactiveButtons:
                        self.backgroundLayer()
            updateRect = Rect(button.xLocation, button.yLocation, button.width, button.height)
            pygame.display.update(updateRect)

    def listenButton(self):  # keyboard shortcuts
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:  # escape to quit
            if self.quitGame in self.activeButtons:
                self.mouseClick(self.quitGame)
        if key[pygame.K_q]:  # escape to quit current stage
            if self.goBack in self.activeButtons:
                self.mouseClick(self.goBack)
        if key[pygame.K_s]:  # s to skip
            if self.skip in self.activeButtons:
                self.mouseClick(self.skip)
        if key[pygame.K_BACKSPACE]:  # backspace to say maybe not
            if self.nevermind in self.activeButtons:
                self.mouseClick(self.nevermind)
        if key[pygame.K_RETURN]:  # return (enter) to say ok
            if self.okay in self.activeButtons:
                self.mouseClick(self.okay)

    def mouseClick(self, button):  # event handler for button press
        if button.buttonText in ["QUIT", "SKIP", "BACK"]:
            self.selectedButtonName = self.warningMessage(button)
        if button.buttonText == "MAYBE NOT":
            self.neverMind()
        if button.buttonText == "OK":
            if self.selectedButtonName == "QUIT":
                self.exitGame()
            if self.selectedButtonName == "SKIP":
                self.skipStage()
            if self.selectedButtonName == "BACK":
                self.exitStage()

    def exitGame(self):  # ToDo: Exit to main menu
        self.makeGreen()

    def skipStage(self):  # ToDo: Exit to map, map node skipped
        self.makeGreen()

    def exitStage(self):  # i.e. goBack # ToDo: Exit to map, map node 'unentered'
        self.makeGreen()

    def neverMind(self):  # Resets the basic Stage background
        self.activeButtons = [self.quitGame, self.goBack, self.skip]
        self.selectedButtonName = None
        self.mainLoop()

    def makeGreen(self):  # A filler function to end the stage
        green = (0, 255, 0)
        self.display.fill(green)
        pygame.display.update()
        self.activeButtons = [self.quitGame, self.goBack, self.skip]
        self.selectedButtonName = None
        pygame.quit()
        exit(0)

    def backgroundLayer(self):  # creates the background of the Stage

        self.display.blit(self.bgImage, (0, 0))
        for button in self.activeButtons + self.inactiveButtons:
            self.displayButton(button)
        pygame.display.update()

    def mainLoop(self):  # listens for events

        self.backgroundLayer()

        mainLoop = True

        while mainLoop:
            self.listenMouse()
            self.listenButton()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainLoop = False

