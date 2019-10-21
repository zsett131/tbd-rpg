from Item import Item

class ConsumableHealingItem(Item):

    healAmount = 0
    Affect = 1

    def __init__(self, name, desc, stackCap, stack, heal, dropRate):
        Item.__init__(name, desc, stackCap, stack, dropRate)

    # Getter and setter for the amount healed
    def sethealAmount(self, heal):
        self.healAmount = heal

    def gethealAmount(self):
        return self.healAmount

    # Getter for Affect
    def getAffect(self):
        return self.Affect
