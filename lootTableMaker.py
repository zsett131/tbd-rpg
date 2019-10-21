from pip._vendor.msgpack.fallback import xrange
import Item
import ConsumableItemsList

class lootTableMaker():

    loot = []

    def __init__(self, *args):
        for x in xrange(*args):
            self.loot.append(args)

    def getLootTable(self):
        return self.loot