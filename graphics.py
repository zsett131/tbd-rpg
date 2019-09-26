import pygame
import sys

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

def sans(x, y):
    gameDisplay.blit(sansRick, (x, y))
def hover(x, y):
    gameDisplay.blit(hoverGriff, (x,y))
def brokenBeter(x,y):
    gameDisplay.blit(familyguy, (x,y))

sansrick_displayx = 250
sansrick_displayy = 300


# -------------------------------------Game Loop
while True:

    # ---------------------------------While statement dies when X button pressed
    pygame.init()
    if not Peter:
        # ---------------------------------Sets Display height and the display button
        gameDisplay = pygame.display.set_mode((display_width, display_height))
        gameDisplay.fill(blue)
        sans(sansrick_displayx, sansrick_displayy)

        # ---------------------------------Grabs the position of the mouse to update the button to sans or peter
        # ---------------------------------Original picture is sansrick, then hovered it's sanspeter,
        # ---------------------------------then when clicked it's just peter pausing the game there.
        mouse = pygame.mouse.get_pos()
        if 250 < mouse[0] < 550 and 300 < mouse[1] < 400:
            hover(sansrick_displayx, sansrick_displayy)
        else:
            sans(sansrick_displayx,sansrick_displayy)
        if pygame.mouse.get_pressed()[0] == 1:
            Peter = True
            brokenBeter(0,0)

    # ---------------------------------Updated the display
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()



