import pygame
from game.base import MakeButton
from game.battle.Battle import Battle
from game.battle.Frame import Frame
from game.base.PlayerBase import PlayerBase
from game.enemy.EnemyList import EnemyList
from game.base import Animation
from game.base import InputField
from game.locations.starting_town import starting_town

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
red = (255, 0, 0)
green = (0, 255, 0)
orange = (255, 140, 0)
blue = (0, 0, 255)
lightblue = (135, 206, 250)
white = (255, 255, 255)
black = (0, 0, 0)
sansrick_displayx = 250
sansrick_displayy = 300
sansRick = pygame.image.load('sansrick.jpg')
hoverGriff = pygame.image.load('hovergriff.jpg')
familyguy = pygame.image.load('familyguypeter.jpg')

The_Player = None
enemies = None
The_Enemy = None
battle_frame = None

def brokenBeter(display, x,y):
    display.blit(familyguy, (x,y))

class GameBase:
    CLICK_STATE = False
    mapLocation = None
    The_Player = PlayerBase("Jairo")
    enemies = EnemyList(The_Player.getPlayerLevel())
    The_Enemy = enemies.ListofEnemies[3]

    def __init__(self):
        self.display = None
        self.clock = pygame.time.Clock()
        self.startButton = MakeButton.MakeButton(self, 300, 100, 400, 400, True, 'sansrick.jpg', 'hovergriff.jpg',
                                                 callback=self.initialGame)
        self.warned = False
        self.nameInput = None

    def initialGame(self):
        print(pygame.font.get_fonts())
        self.startButton.hide()
        self.nameInput = InputField.InputField(self, 400, 300, 425, 50, 45, maxLength=15, space=False, callback=self.enterGame)
        self.nameInput.show()
        self.drawInstruction()
        buttonText = pygame.font.SysFont('cambriacambriamath', 60).render('Enter⏎', True, black)
        self.nameInputButton = MakeButton.MakeButton(self, 200, 75, 400, 400, True, standard_img=None, hover_img=None,
                                                     text=buttonText, callback=self.enterGame)
        self.nameInputButton.show()
        InputField.SELECTED = self.nameInput

    def enterGame(self):
        self.The_Player.setPlayerName(self.nameInput.textInput.get_text())
        self.nameInput.hide()
        self.nameInputButton.hide()
        InputField.SELECTED = None
        self.nameInput = None
        self.nameInputButton = None
        self.testMap()

    def drawInstruction(self):
        self.display.fill(black)
        instructFont = pygame.font.SysFont('comicsansms', 30)
        instructText = instructFont.render("Please enter a name for your character.", True, white)
        self.display.blit(instructText, (400 - instructText.get_width() / 2, 200))

    def testMap(self):
        self.mapLocation = starting_town(self.The_Player, self, 'StartingTown.png')
        self.mapLocation.addButtons()
        self.mapLocation.showMainButtons()
        self.startButton.hide()

    def exception(self):
        brokenBeter(self.display, 0, 0)
        for button in MakeButton.BUTTONS:
            button.hide()

    def peterTime(self):
        brokenBeter(self.display, 0, 0)
        self.startButton.hide()

        # --------------------------------------Initiates the battle phase, will be placed into another class later.
        Frame.efill(self, black)
        battle_frame = Battle(self.The_Player, self.The_Enemy, self)
        self.The_Player = battle_frame.battleComplete()

    def battleTime(self, enemy):
        battle_frame = Battle(self.The_Player, enemy, self)

    def construct(self):
        self.display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    def updateDisplay(self):
        pygame.display.update()

    def run(self):
        self.construct()
        self.display.fill(blue)
        quit = False
        self.startButton.show()
        while not quit:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if InputField.SELECTED and InputField.SELECTED == self.nameInput:
                        if event.key == pygame.K_BACKSPACE:
                            self.drawInstruction()
                        elif len(self.nameInput.textInput.get_text()) >= self.nameInput.textInput.max_string_length:
                            warnFont = pygame.font.Font(None, 30)
                            warnText = warnFont.render('You have reached the maximum name length.', True, red)
                            self.display.blit(warnText, (400 - warnText.get_width() / 2, 245))
                if event.type == pygame.QUIT:
                    quit = True

            for button in MakeButton.BUTTONS:
                button.process()

            for process in Animation.PROCESSING:
                process.process()

            for field in InputField.FIELDS:
                field.process(events)

            if pygame.mouse.get_pressed()[0]:
                self.CLICK_STATE = True
            else:
                self.CLICK_STATE = False

            self.clock.tick(30)


            # ---------------------------------While statement dies when X button pressed
            pygame.display.update()

