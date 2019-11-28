"""
Main module for starting the game.
__authors__: Jairo Garciga and Zachary Setterquist
"""
from game.base import GameBase
import pygame
from game.characters.PlayerBase import PlayerBase
import traceback

Player = PlayerBase("Jairo")

clock = pygame.time.Clock()
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

white = (255, 255, 255)
black = (0, 0, 0)
display_height = 600
display_width = 800

sansRick = pygame.image.load('Images/sansrick.jpg')
hoverGriff = pygame.image.load('Images/hovergriff.jpg')
familyguy = pygame.image.load('Images/familyguypeter.jpg')
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
    QUIT = False
    while not QUIT:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QUIT = True

        if pygame.mouse.get_pressed()[0]:
            QUIT = True

pygame.quit()
