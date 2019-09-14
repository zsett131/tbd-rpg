from random import random
from pip._vendor.msgpack.fallback import xrange
import Item
import ConsumableItemsList

class lootTableMaker():

    loot = []
    dropRate = 0

    def __init__(self, *args):
        for x in xrange(*args):
            self.loot.append(args)

    def getLootTable(self):
        return self.loot

    def getDropChance(self, index):
        dropRate = ((index+1)**2)//(len(self.loot)*10)

    def didlootDrop(self):
        die = random()
        if die <= self.dropRate:
            return True
        else:
            return False