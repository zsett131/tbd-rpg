"""
The class that creates the major frames for the battles.
Both the top and bottom halves and their subsequent buttons.
__author__: Jairo Garciga and Zachary Setterquist
"""
from game.base.MakeButton import MakeButton
from game.base import GameBase
from game.base.Animation import TextWriter
import pygame


class Frame:
    def __init__(self, down, right, gamebase, battle):
        self.down = down
        self.right = right
        self.mainGame = gamebase
        self.battle = battle
        self.display = self.mainGame.display
        self.buttons = []
        self.attackButton = None
        self.runButton = None
        self.itemButton = None
        self.cringeButton = None
        self.backButton = None
        self.attack1 = None
        self.attack2 = None
        self.attack3 = None
        self.attack4 = None
        self.postBattleDeath = None
        self.color = None
        self.width = None
        self.depth = None
        self.textWriter = None
        self.playerDialogText = ''
        self.enemyDialogText = ''
        self.myFont = pygame.font.SysFont('Comic Sans TM', 25)
        self.deathMessage = "You died :("
        self.victoryMessage = "You Won!"

    def efill(self, color):
        self.display.fill(color)

    def make_rect(self, color, width, depth):
        self.color = color
        self.width = width
        self.depth = depth
        pygame.draw.rect(self.display, color,
                         (self.right, self.down, width, depth))

    def unique_rect(self, color, right, down, width, depth):
        pygame.draw.rect(self.display, color, (right, down, width, depth))

    def add_buttons(self):
        self.attackButton = MakeButton(self.mainGame,
                                       callback=self.enter_attack, width=250,
                                       height=100, desired_x=200,
                                       desired_y=375, visibility=True,
                                       standard_img=None, hover_img=None,
                                       text=self.battle.button_font.render(
                                           'Attack', True, GameBase.black))
        self.runButton = \
            MakeButton(self.mainGame,
                       callback=self.return_to_location, width=250,
                       height=100,
                       desired_x=600, desired_y=375,
                       visibility=True, standard_img=None,
                       hover_img=None,
                       text=self.battle.button_font.render('Run',
                                                           True,
                                                           GameBase.black))
        self.itemButton = MakeButton(self.mainGame,
                                     callback=lambda: print(self.battle, '3'),
                                     width=250, height=100,
                                     desired_x=200, desired_y=525,
                                     visibility=True, standard_img=None,
                                     hover_img=None,
                                     text=self.battle.button_font.render(
                                         'Item', True, GameBase.black))
        self.cringeButton = MakeButton(self.mainGame,
                                       callback=lambda: print(self.battle,
                                                              '4'), width=250,
                                       height=100,
                                       desired_x=600, desired_y=525,
                                       visibility=True, standard_img=None,
                                       hover_img=None)
        self.backButton = MakeButton(self.mainGame, callback=self.exit_attack,
                                     width=25, height=25, desired_x=25,
                                     desired_y=325, visibility=True,
                                     standard_img='exit_normal.png',
                                     hover_img='exit_hover.png')
        self.attack1 = MakeButton(self.mainGame, callback=self.do_attack,
                                  width=250, height=100,
                                  desired_x=200, desired_y=375,
                                  visibility=True, standard_img=None,
                                  hover_img=None)
        self.attack2 = MakeButton(self.mainGame,
                                  callback=lambda: print(self.battle,
                                                         'attack-2'),
                                  width=250, height=100,
                                  desired_x=600, desired_y=375,
                                  visibility=True, standard_img=None,
                                  hover_img=None)
        self.attack3 = MakeButton(self.mainGame,
                                  callback=lambda: print(self.battle,
                                                         'attack-3'),
                                  width=250, height=100,
                                  desired_x=200, desired_y=525,
                                  visibility=True, standard_img=None,
                                  hover_img=None)
        self.attack4 = MakeButton(self.mainGame,
                                  callback=lambda: print(self.battle,
                                                         'attack-4'),
                                  width=250, height=100,
                                  desired_x=600, desired_y=525,
                                  visibility=True, standard_img=None,
                                  hover_img=None)
        self.postBattleDeath = MakeButton(self.mainGame,
                                          callback=self.return_to_location,
                                          width=250, height=200,
                                          desired_x=400, desired_y=450,
                                          visibility=True, standard_img=None,
                                          hover_img=None,
                                          text=self.battle.button_font.render(
                                              self.victoryMessage, True,
                                              GameBase.red))
        self.show_main()

    def show_main(self):
        self.make_rect(self.color, self.width, self.depth)
        self.attackButton.show()
        self.runButton.show()
        self.itemButton.show()
        self.cringeButton.show()

    def return_to_location(self):
        self.attackButton.hide()
        self.runButton.hide()
        self.itemButton.hide()
        self.cringeButton.hide()
        self.postBattleDeath.hide()
        self.display.blit(self.mainGame.mapLocation.locationMap, (0, 0))
        self.mainGame.mapLocation.show_main_buttons()

    def enter_attack(self):
        self.attackButton.hide()
        self.runButton.hide()
        self.itemButton.hide()
        self.cringeButton.hide()
        self.make_rect(self.color, self.width, self.depth)
        self.backButton.show()
        self.attack1.show()
        self.attack2.show()
        self.attack3.show()
        self.attack4.show()

    def exit_attack(self):
        self.backButton.hide()
        self.attack1.hide()
        self.attack2.hide()
        self.attack3.hide()
        self.attack4.hide()
        self.make_rect(self.color, self.width, self.depth)
        self.show_main()

    def do_attack(self):
        self.backButton.hide()
        self.attack1.hide()
        self.attack2.hide()
        self.attack3.hide()
        self.attack4.hide()
        self.make_rect(self.color, self.width, self.depth)
        self.do_player_dialog()

    def set_player_dialog(self, text):
        self.playerDialogText = text
        self.make_rect(self.color, self.width, self.depth)
        text = self.myFont.render(self.playerDialogText, True, GameBase.white)
        self.display.blit(text, (20, 310))
        if self.playerDialogText == self.textWriter.text:
            self.battle.theEnemy.enemy_take_damage(
                self.battle.thePlayer.get_player_damage())
            self.battle.draw_health_bars()
            self.mainGame.update_display()
            if self.battle.theEnemy.get_hp() <= 0:
                self.postBattleDeath.text = self.battle.button_font.render(
                    self.victoryMessage, True, GameBase.red)
                self.postBattleDeath.show()
            else:
                self.do_enemy_dialog()

    def set_enemy_dialog(self, text):
        self.enemyDialogText = text
        self.make_rect(self.color, self.width, self.depth)
        text1 = self.myFont.render(self.playerDialogText, True, GameBase.white)
        text2 = self.myFont.render(self.enemyDialogText, True, GameBase.white)
        self.display.blit(text1, (20, 310))
        self.display.blit(text2, (20, 340))
        if self.enemyDialogText == self.textWriter.text:
            self.battle.thePlayer.player_take_damage(
                self.battle.theEnemy.get_damage())
            self.battle.draw_health_bars()
            self.mainGame.update_display()
            if self.battle.thePlayer.get_player_current_health() <= 0:
                self.battle.thePlayer.set_player_current_health(
                    (self.battle.thePlayer.get_player_max_health() // 3) + 1)
                self.postBattleDeath.text = self.battle.buttonfont.render(
                    self.deathMessage, True, GameBase.red)
                self.postBattleDeath.show()
            else:
                self.textWriter = None
                self.playerDialogText = None
                self.enemyDialogText = None
                self.show_main()

    def do_player_dialog(self):
        firstAttack = self.battle.thePlayer.get_player_name() \
                      + " has dealt " + str(
            self.battle.thePlayer.get_player_damage()) + \
                      " to " + self.battle.theEnemy.get_name()
        self.textWriter = TextWriter(self.mainGame, 30, firstAttack,
                                     self.set_player_dialog)
        self.textWriter.start()

    def do_enemy_dialog(self):
        secondAttack = self.battle.theEnemy.get_name() + " has dealt " + \
                       str(
                           self.battle.theEnemy.get_damage()) + " to " + \
                       self.battle.thePlayer.get_player_name()
        self.textWriter = TextWriter(self.mainGame, 30, secondAttack,
                                     self.set_enemy_dialog)
        self.textWriter.start()
