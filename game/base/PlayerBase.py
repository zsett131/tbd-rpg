"""
This is the object for the player and stores hp, exp, items, and stats.
__author__: Jairo Garciga and Zachary Setterquist
"""

import pygame
import math
from game.base.MakeButton import MakeButton
from game.inventory import Item

pygame.init()
my_font = pygame.font.SysFont('comicsansms', 16)
white = (255, 255, 255)
black = (0, 0, 0)


class PlayerBase:
    """
    This class sets up the player object which is used throughout the program.
    """

    def __init__(self, name):
        """
        :param name: place holder for the name
        All the other variables are being called for initialization.
        """
        # Player stats and attributes
        self.playerName = name
        self.playerAlive = True
        self.playerIcon = pygame.image.load('Images/Jotaro.jpg')
        self.playerLevel = 1
        self.playerExp = 0
        self.playerExpCap = 100
        self.playerHealthPercentage = 0.0
        self.expLogistic = 0
        self.playerCurrentHealth = 200
        self.playerMaxHealth = 200
        self.playerWeapon = Item
        self.playerDamage = 100
        self.playerInventory = []
        self.display = None
        self.base = None
        self.level_up_button_Strength = None
        self.level_up_button_Agility = None
        self.level_up_button_Wisdom = None
        self.exit_level_up = None

        # The stats, strength, wisdom, and agility.

        self.strength = 0
        self.wisdom = 0
        self.agility = 0
        self.skillPoints = 0

    def exp_algorithm(self):
        """
        Creates the logistical function for percent increase in exp.
        :return: percentage increase for the exp cap.
        """
        exp_logistic = 1 / (
                3 + math.exp(-(3 / 4) * (self.playerLevel / 16) - 4)) + 1
        return exp_logistic

    def set_player_name(self, input_name):
        """
        Sets the player's name to the input
        :param input_name: Takes input for the name
        """
        self.playerName = input_name

    def get_player_name(self):
        """
        Outputs player's name
        :return: the player's name
        """
        return self.playerName

    def get_player_level(self):
        """
        Gets player's level
        :return: player level
        """
        return self.playerLevel

    def player_level_up(self):
        """
        Levels up the player WIP
        """
        while self.get_player_exp() >= self.get_player_exp_cap():
            self.playerLevel += 1
            self.increment_skill_points()
            self.set_player_exp(
                self.get_player_exp() - self.get_player_exp_cap())
            self.set_player_exp_cap()

    def player_level_up_screen(self, base):
        """
        This function calls a new display that allows for the player to
        decide where to add skill points in.
        :param base: The GameBase object
        """

        self.base = base

        self.level_up_button_Strength = \
            MakeButton(base, callback=self.increase_player_strength,
                       width=200, height=100,
                       desired_x=500, desired_y=200,
                       hover_img=None, standard_img=None,
                       visibility=True,
                       text=my_font.render(
                           'Strength', True, black))

        self.level_up_button_Agility = \
            MakeButton(base, callback=self.increase_player_agility,
                       width=200, height=100,
                       desired_x=500, desired_y=325,
                       hover_img=None, standard_img=None,
                       visibility=True,
                       text=my_font.render(
                           'Agility', True, black))

        self.level_up_button_Wisdom = \
            MakeButton(base, callback=self.increase_player_wisdom,
                       width=200, height=100,
                       desired_x=500, desired_y=450,
                       hover_img=None, standard_img=None,
                       visibility=True,
                       text=my_font.render(
                           'Wisdom', True, black))

        self.exit_level_up = \
            MakeButton(base, callback=self.player_exit_level_up_screen,
                       width=150, height=50,
                       desired_x=700, desired_y=50,
                       hover_img=None, standard_img=None,
                       visibility=True,
                       text=my_font.render(
                           'Return to location', True, black))

        self.display = base.display
        self.level_up_button_Strength.show()
        self.level_up_button_Agility.show()
        self.level_up_button_Wisdom.show()
        self.exit_level_up.show()
        self.display.fill(black)
        pygame.draw.rect(self.display, white, (100, 150, 200, 350))
        bruh = my_font.render(self.get_player_name() + "'s Stats", True, black)
        strength = my_font.render(("Strength:" + str(self.strength)),
                                  True, black)
        agility = my_font.render(("Agility:" + str(self.agility)),
                                 True, black)
        wisdom = my_font.render(("Wisdom:" + str(self.wisdom)),
                                True, black)

        self.display.blit(bruh, (200 - bruh.get_rect().width / 2, 175))
        self.display.blit(strength, (200 - bruh.get_rect().width / 2, 250))
        self.display.blit(agility, (200 - bruh.get_rect().width / 2, 325))
        self.display.blit(wisdom, (200 - bruh.get_rect().width / 2, 400))

    def update_player_level_up_screen(self):
        """
        Quickly updates the stats side of the level up screen
        """
        pygame.draw.rect(self.display, white, (100, 150, 200, 350))
        bruh = my_font.render(self.get_player_name() + "'s Stats", True, black)
        strength = my_font.render(("Strength:" + str(self.strength)),
                                  True, black)
        agility = my_font.render(("Agility:" + str(self.agility)),
                                 True, black)
        wisdom = my_font.render(("Wisdom:" + str(self.wisdom)),
                                True, black)
        self.display.blit(bruh, (200 - bruh.get_rect().width / 2, 175))
        self.display.blit(strength, (200 - bruh.get_rect().width / 2, 250))
        self.display.blit(agility, (200 - bruh.get_rect().width / 2, 325))
        self.display.blit(wisdom, (200 - bruh.get_rect().width / 2, 400))
        pygame.display.update()

    def player_exit_level_up_screen(self):
        """
        This is a function that exits the level up screen.
        """
        self.level_up_button_Strength.hide()
        self.level_up_button_Agility.hide()
        self.level_up_button_Wisdom.hide()
        self.exit_level_up.hide()
        self.display.blit(self.base.mapLocation.locationMap, (0, 0))
        self.base.mapLocation.show_main_buttons()

    # Player Exp Setter and Getter.

    def add_player_exp(self, exp_gained):
        """
        Adds exp to the player's exp and levels up if necessary
        :param exp_gained: exp increase amount
        """
        self.playerExp += exp_gained
        self.player_level_up()

    def set_player_exp(self, amount):
        """
        Sets the Player's exp
        :param amount: the amount of exp
        """
        self.playerExp = amount

    def get_player_exp(self):
        """
        Returns the Player's exp
        :return: player exp
        """
        return self.playerExp

    def set_player_exp_cap(self):
        """
        Sets the exp cap each time in relation to player level
        """
        self.playerExpCap = int(self.playerExpCap * self.exp_algorithm())

    def get_player_exp_cap(self):
        """
        Returns player exp cap
        :return: the player exp cap
        """
        return self.playerExpCap

    def set_player_current_health(self, incoming):
        """
        Sets the current health of the player to the incoming number,
        either adding or subtracting
        :param incoming: number health changing by
        """
        self.playerCurrentHealth = incoming

    def get_player_current_health(self):
        """
        Outputs player's current health and checks if player is alive
        :return: player's current health
        """
        return self.playerCurrentHealth

    def player_heal(self, amount):
        """
        Heals the player's health by adding the current health and the
        health amount together.
        At most it can be the max health.
        :param amount: Amount of health the player is healed
        """
        if amount + self.get_player_current_health() <= \
                self.get_player_max_health():
            self.set_player_current_health(self.get_player_current_health() +
                                           amount)
        else:
            self.set_player_current_health(self.get_player_max_health())

    def set_player_health_max(self):
        """
        Automatically sets the player's current health to max.
        """
        self.set_player_current_health(self.get_player_max_health())

    def player_take_damage(self, damage):
        """
        Reduces the health of the player based on incoming damage.
        :param damage: The amount of damage the player is taking
        """
        if self.playerCurrentHealth - damage > 0:
            self.playerCurrentHealth = self.get_player_current_health() - \
                                       damage
        elif self.playerCurrentHealth - damage <= 0:
            self.playerCurrentHealth = 0

    def is_player_alive(self):
        """
        Determines if the player is alive
        :return: Boolean depending on player hp being 0 or not
        """
        if self.get_player_current_health() == 0:
            self.playerAlive = False
            return False
        else:
            return True

    def set_player_max_health(self):
        """
        Sets the maximum health of the player
        """
        self.playerMaxHealth = (
            self.get_player_max_health())

    def get_player_max_health(self):
        """
        Returns the player's maximum health
        :return: The player's maximum health value
        """
        return self.playerMaxHealth

    def set_player_health_percentage(self):
        """
        Creates a percentage of the current player health divided by the
        maximum player health.
        """
        self.playerHealthPercentage = (self.get_player_current_health()
                                       / self.get_player_max_health())

    def get_player_health_percentage(self):
        """
        Returns the health percentage
        :return: percentage of health the player has
        """
        self.set_player_health_percentage()
        return self.playerHealthPercentage

    # Sets and Gets the players equipped item
    def set_player_equipped(self, weapon):
        """
        Sets the item that the player has equipped
        :param weapon: The item
        """
        if self.get_player_equipped():
            self.set_player_damage(
                weapon.get_damage())  # * (1 + (self.get_player_strength() //
            # 10)))
        else:
            self.set_player_damage(1)  # + (self.get_player_strength() // 10))

    def get_player_equipped(self):
        """
        Returns the item the player has equipped
        :return: player weapon
        """
        return self.playerWeapon

    # Player damage Setter and Getter.

    def set_player_damage(self, damage):
        """
        Assigns the player's damage to the parameter damage
        :param damage: the amount of damage
        """
        self.playerDamage = damage

    def get_player_damage(self):
        """
        Returns the player's damage
        :return: player's damage
        """
        return self.playerDamage

    def increment_skill_points(self):
        """
        Increases the player's skill points by one
        """
        self.skillPoints += 1
        print("You have accrued one more skill point.")

    def set_skill_points(self, allocation):
        """
        Sets the player's skill points to the parameter allocation
        :param allocation: The amount of skill points
        """
        self.skillPoints += allocation

    def allocate_skill_points(self):
        """
        Subtracts skill points from the total skill points to "allocate"
        :param: Skill points being allocated
        """
        self.skillPoints -= 1

    def get_skill_points(self):
        """
        Returns the amount of skill points
        :return: the player's skill points
        """
        return self.skillPoints

    def increase_player_strength(self):
        """
        Increases the player's strength by one.
        """
        if self.get_skill_points() > 0:
            self.allocate_skill_points()
            self.strength += 1
            self.update_player_level_up_screen()

    def increase_player_agility(self):
        """
        Increases the player's agilit by one.
        """
        if self.get_skill_points() > 0:
            self.allocate_skill_points()
            self.agility += 1
            self.update_player_level_up_screen()

    def increase_player_wisdom(self):
        """
        Increases the player's wisdom by one.
        """
        if self.get_skill_points() > 0:
            self.allocate_skill_points()
            self.wisdom += 1
            self.update_player_level_up_screen()

    # The mythical land of player inventory. Appends to list and also
    # removes based on function.

    def add_to_player_inventory(self, item):
        """

        :param item:
        """
        self.playerInventory.append(item)

    def get_from_player_inventory(self, position):
        """

        :param position:
        :return:
        """
        return self.playerInventory[position]

    def remove_from_player_inventory(self, removal_point):
        """

        :param removal_point:
        """
        self.playerInventory.remove(removal_point)

    def get_player_inventory(self):
        """

        :return:
        """
        return self.playerInventory
