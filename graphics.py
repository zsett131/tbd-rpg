import pygame
import sys
<<<<<<< HEAD
import time
from EnemyList import ListofEnemies
from PlayerBase import PlayerBase
from makeButton import makeButton
from Battle import Battle

Player = PlayerBase("Jairo")
import GameBase
from Frame import Frame

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
base.run()
pygame.quit()
