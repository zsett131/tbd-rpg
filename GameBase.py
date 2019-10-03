import pygame
import MakeButton
from Frame import Frame

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
sansrick_displayx = 250
sansrick_displayy = 300
sansRick = pygame.image.load('sansrick.jpg')
hoverGriff = pygame.image.load('hovergriff.jpg')
familyguy = pygame.image.load('familyguypeter.jpg')

def brokenBeter(display, x,y):
    display.blit(familyguy, (x,y))

class GameBase:

    def __init__(self):
        self.display = None
        self.clock = pygame.time.Clock()
        self.startButton = MakeButton.MakeButton(self, 300, 100, 400, 400, 'sansrick.jpg', 'hovergriff.jpg',
                                                 callback=self.peterTime)

    def peterTime(self):
        brokenBeter(self.display, 0, 0)
        self.startButton.hide()

        # --------------------------------------Initiates the battle phase, will be placed into another class later.
        Frame.efill(self, black)
        battle_frame = Frame(300, 0, self)
        battle_frame.makeRect(blue, 800, 300)

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


            self.clock.tick(30)

            # ---------------------------------While statement dies when X button pressed
            pygame.display.update()

