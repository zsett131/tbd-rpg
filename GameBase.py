import pygame
import MakeButton
from Battle import Battle
from Frame import Frame
from PlayerBase import PlayerBase
from EnemyBasic import EnemyBasic
from EnemyList import ListofEnemies

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
lightblue = (135, 206, 250)
white = (255, 255, 255)
black = (0, 0, 0)
sansrick_displayx = 250
sansrick_displayy = 300
sansRick = pygame.image.load('sansrick.jpg')
hoverGriff = pygame.image.load('hovergriff.jpg')
familyguy = pygame.image.load('familyguypeter.jpg')

The_Player = PlayerBase("Jairo")
The_Enemy = ListofEnemies[0]
battle_frame = None

def brokenBeter(display, x,y):
    display.blit(familyguy, (x,y))

class GameBase:
    CLICK_STATE = False

    def __init__(self):
        self.display = None
        self.clock = pygame.time.Clock()
        self.startButton = MakeButton.MakeButton(self, 300, 100, 400, 400, 'sansrick.jpg', 'hovergriff.jpg',
                                                 callback=self.peterTime)

    def exception(self):
        brokenBeter(self.display, 0, 0)
        for button in MakeButton.BUTTONS:
            button.hide()

    def peterTime(self):
        brokenBeter(self.display, 0, 0)
        self.startButton.hide()

        # --------------------------------------Initiates the battle phase, will be placed into another class later.
        Frame.efill(self, black)
        battle_frame = Battle(The_Player, The_Enemy, self)

    def construct(self):
        self.display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    def run(self):
        self.construct()
        self.display.fill(blue)
        quit = False
        self.startButton.show()
        while not quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit = True

            for button in MakeButton.BUTTONS:
                button.process()

            if pygame.mouse.get_pressed()[0]:
                self.CLICK_STATE = True
            else:
                self.CLICK_STATE = False

            self.clock.tick(30)


            # ---------------------------------While statement dies when X button pressed
            pygame.display.update()

