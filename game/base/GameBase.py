"""
The main loop of the game
"""
import pygame
from game.base import MakeButton
from game.battle.Battle import Battle
from game.base.PlayerBase import PlayerBase
from game.enemy.EnemyList import EnemyList
from game.base import Animation
from game.base import InputField
from game.locations.StartingTown import StartingTown

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
red = (255, 0, 0)
green = (0, 255, 0)
orange = (255, 140, 0)
blue = (0, 0, 255)
light_blue = (135, 206, 250)
white = (255, 255, 255)
black = (0, 0, 0)
sansrick_display_x = 250
sansrick_display_y = 300
sansRick = pygame.image.load('sansrick.jpg')
hoverGriff = pygame.image.load('hovergriff.jpg')
familyguy = pygame.image.load('familyguypeter.jpg')

The_Player = None
enemies = None
The_Enemy = None
battle_frame = None


def broken_beter(display, x, y):
    """
    Sets the crash screen and displays it
    :param display: The GameBase
    :param x: x-coordinate
    :param y: y-coordinate
    """
    display.blit(familyguy, (x, y))


class GameBase:
    """
    The main screen of the game with the main loop
    """
    CLICK_STATE = False
    mapLocation = None
    The_Player = PlayerBase("Jairo")
    enemies = EnemyList(The_Player.get_player_level())
    The_Enemy = enemies.list_of_enemies[3]

    def __init__(self):
        self.display = None
        self.clock = pygame.time.Clock()
        self.startButton = MakeButton.MakeButton(self, 300, 100, 400, 400,
                                                 True, 'sansrick.jpg',
                                                 'hovergriff.jpg',
                                                 callback=self.initial_game)
        self.buttonText = pygame.font.SysFont('cambriacambriamath', 60).render(
            'Enter⏎', True, black)
        self.nameInputButton = None
        self.game_battle = None
        self.warned = False
        self.nameInput = None

    def initial_game(self):
        """
        The initial launch of the game, with the main start button.
        """
        print(pygame.font.get_fonts())
        self.startButton.hide()
        self.nameInput = InputField.InputField(self, 400, 300, 425, 50, 45,
                                               max_length=15, space=False,
                                               callback=self.enter_game)
        self.nameInput.show()
        self.draw_instruction()
        self.nameInputButton = MakeButton.MakeButton(self, 200, 75, 400, 400,
                                                     True, standard_img=None,
                                                     hover_img=None,
                                                     text=self.buttonText,
                                                     callback=self.enter_game)
        self.nameInputButton.show()
        InputField.SELECTED = self.nameInput

    def enter_game(self):
        """
        Enters into the game
        Take the name input
        """
        self.The_Player.set_player_name(self.nameInput.textInput.get_text())
        self.nameInput.hide()
        self.nameInputButton.hide()
        InputField.SELECTED = None
        self.nameInput = None
        self.nameInputButton = None
        self.test_map()

    def draw_instruction(self):
        """
        Draws the name input screen and text.
        """
        self.display.fill(black)
        instruct_font = pygame.font.SysFont('comicsansms', 30)
        instruct_text = instruct_font.render(
            "Please enter a name for your character.", True, white)
        self.display.blit(instruct_text,
                          (400 - instruct_text.get_width() / 2, 200))

    def test_map(self):
        """
        Initializes the first map and all of it's buttons
        """
        self.mapLocation = StartingTown(self.The_Player, self,
                                        'StartingTown.png')
        self.mapLocation.show_main_buttons()
        self.startButton.hide()

    def exception(self):
        """
        The recovery if some functions go bad or if something crashes.
        """
        broken_beter(self.display, 0, 0)
        for button in MakeButton.BUTTONS:
            button.hide()

    def peter_time(self):
        """
        Crash button
        """
        broken_beter(self.display, 0, 0)
        self.startButton.hide()

    def battle_time(self, enemy):
        """
        Initializes each battle and enemy.
        :param enemy: The enemy
        """
        enemy.set_enemy_health_to_max()
        self.game_battle = Battle(self.The_Player, enemy, self)

    def construct(self):
        """
        Constructs the display of the game and sets it
        """
        self.display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    @staticmethod
    def update_display():
        """
        Updates the display
        :return:
        """
        pygame.display.update()

    def run(self):
        """
        The main loop of the game that registers button presses.
        """
        self.construct()
        self.display.fill(blue)
        quit_event = False
        self.startButton.show()
        while not quit_event:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if InputField.SELECTED and InputField.SELECTED == \
                            self.nameInput:
                        if event.key == pygame.K_BACKSPACE:
                            self.draw_instruction()
                        elif len(
                                self.nameInput.textInput.get_text()) >= \
                                self.nameInput.textInput.max_string_length:
                            warn_font = pygame.font.Font(None, 30)
                            warn_text = warn_font.render(
                                'You have reached the maximum name length.',
                                True, red)
                            self.display.blit(warn_text, (
                                400 - warn_text.get_width() / 2, 245))
                if event.type == pygame.QUIT:
                    quit_event = True

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

            # While statement dies when X button pressed
            pygame.display.update()
