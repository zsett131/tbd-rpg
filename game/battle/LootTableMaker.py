"""
This class creates a loot-table for the enemy to use
__author__: Jairo Garciga
"""


class LootTableMaker:
    """
    Makes the loot table
    """
    loot = []

    def __init__(self, *args):
        for x in range(*args):
            self.loot.append(args)

    def get_loot_table(self):
        """
        Returns the loot table for use by whichever enemy it calls
        :return: The loot table
        """
        return self.loot
