"""
The item class and it's children
"""


class Item:
    """
    Parent class for all items
    """
    # All the important variables for a consumable item.
    # The constructor that sets the.
    # name, description, StackCap, Stack, and affect.
    def __init__(self, name, desc, stack_cap, stack, drop_rate):
        self.itemName = name
        self.itemDescription = desc
        self.itemStackCap = stack_cap
        self.itemStack = stack
        self.itemDropRate = drop_rate

    # The setter and Getter for itemName
    def set_item_name(self, name):
        """
        Sets the name of the item, although this seems quite stupid.
        :param name: the name
        """
        self.itemName = name

    def get_item_name(self):
        """
        Returns the name of the item
        :return: the name of the item
        """
        return self.itemName

    # The setter and Getter for itemDescription
    def set_item_description(self, desc):
        """
        sets the description of the item
        :param desc: the item description
        """
        self.itemDescription = desc

    def get_item_description(self):
        """
        Gets the item description
        :return: item description
        """
        return self.itemDescription

    # Setters and Getters for itemStackCap and itemStack
    def set_item_stack_cap(self, cap):
        """
        Sets the max amount of items the player can hold.
        :param cap: The max amount of item.
        """
        self.itemStackCap = cap

    def set_item_stack(self, amount):
        """
        Sets the amount of the item
        :param amount: stack amount
        """
        self.itemStack = amount

    def get_item_stack_cap(self):
        """
        Gets the max item stack
        :return: the max item stak
        """
        return self.itemStackCap

    def get_item_stack(self):
        """
        Gets the item stack
        :return: Gets the item stack
        """
        return self.itemStack

    # Most important function, setter and getter for drop rate.
    def set_item_drop_rate(self, rate):
        """
        Sets the drop rates of the items just in case.
        :param rate: the drop rate
        """
        self.itemDropRate = float(rate)

    def get_item_drop_rate(self):
        """
        Gets the drop rate of the item
        :return: The drop rate
        """
        return self.itemDropRate


class EquippableItem(Item):
    """
    This type of item is equippable by the player, like a sword, ring,
    or helmet.
    """
    def __init__(self, name, desc, level_req, damage, stack_cap,
                 stack, drop_rate):
        Item.__init__(self, name, desc, stack_cap, stack, drop_rate)
        self.level_req = level_req
        self.damage = damage

    def set_level_req(self, level):
        """
        Sets the level requirement, not necessary as it's in the constructor.
        :param level: the item's level
        """
        self.level_req = level

    def get_level_req(self):
        """
        Returns the item's  level
        :return: The item's level
        """
        return self.level_req

    def set_damage(self, damage):
        """
        Sets the damage of the item
        :param damage: item damage
        """
        self.damage = damage

    def get_damage(self):
        """
        Returns the damage of the item
        :return: item damage
        """
        return self.damage
