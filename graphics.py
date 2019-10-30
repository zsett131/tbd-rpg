import pygame
from game.base.PlayerBase import PlayerBase
import traceback

Player = PlayerBase("Jairo")
from game.base import GameBase

clock = pygame.time.Clock()
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

white = (255, 255, 255)
black = (0, 0, 0)
display_height = 600
display_width = 800

sansRick = pygame.image.load('sansrick.jpg')
hoverGriff = pygame.image.load('hovergriff.jpg')
familyguy = pygame.image.load('familyguypeter.jpg')
# The picture that is printed when the game crashes
Peter = False

sansrick_displayx = 250
sansrick_displayy = 300


# -------------------------------------Game Loop
pygame.init()
base = GameBase.GameBase()
try:
    base.run()
except Exception as e:
    print(e)
    base.exception()
    traceback.print_exc()
    pygame.display.update()
    quit = False
    while not quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True

        if pygame.mouse.get_pressed()[0]:
            quit = True

pygame.quit()
