import Item

class ConsumableHealingItem(Item):

    healAmount = 0
    Affect = 1

    def __init__(self, arg1, arg2, arg3, arg4, heal):
        self.sethealAmount(heal)

    # Getter and setter for the amount healed
    def sethealAmount(self, heal):
        self.healAmount = heal

    def gethealAmount(self):
        return self.healAmount

    # Getter for Affect
    def getAffect(self):
        return self.Affect
