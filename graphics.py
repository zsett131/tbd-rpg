import pygame
import sys
from makeButton import makeButton

clock = pygame.time.Clock()
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

white = (255, 255, 255)
black = (0, 0, 0)
display_height = 600
display_width = 800

familyguy = pygame.image.load('familyguypeter.jpg')

Peter = False
sansrick_displayx = 250
sansrick_displayy = 300

startingButton = makeButton(300, 100, 400, 400, 'sansrick.jpg', 'hovergriff.jpg')

# -------------------------------------Game Loop
quit = False
pygame.init()
while not quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

    maxFrames = clock.tick(30)

    # ---------------------------------While statement dies when X button pressed
    if not Peter:
        # ---------------------------------Sets Display height and the display button
        gameDisplay = pygame.display.set_mode((display_width, display_height))
        gameDisplay.fill(blue)
        buttonHover = False
        gameDisplay.blit(startingButton.imgStandard(), startingButton.getXY())

        # ---------------------------------Grabs the position of the mouse to update the button to sans or peter
        # ---------------------------------Original picture is sansrick, then hovered it's sanspeter,
        # ---------------------------------then when clicked it's just peter pausing the game there.

        mouse = pygame.mouse.get_pos()
        if 250 < mouse[0] < 550 and 350 < mouse[1] < 450:
            gameDisplay.blit(startingButton.imgHover(), startingButton.getXY())
            buttonHover = True
        else:
            gameDisplay.blit(startingButton.imgStandard(), startingButton.getXY())
        if pygame.mouse.get_pressed()[0] == 1 and buttonHover:
            Peter = True
            gameDisplay.blit(familyguy, (0,0))

    # ---------------------------------Updated the display
    pygame.display.update()

pygame.quit()



