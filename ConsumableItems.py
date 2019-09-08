import Item
from ConsumableHealingItem import ConsumableHealingItem

class ConsumableItems():

    consumables = []

    # This initializes the items within consumables[], and then returns the one that is asked
    # for in the position argument.
    def __init__(self, position):
        self.setConsumables()
        self.getConsumable(position)

    # This is the crucial method for the consumable items. Here is where each consumable item is stored.
    def setConsumables(self):

        self.consumables.append(ConsumableHealingItem("Health Potion", "A potion that heals for 10 health.", 10, 1, 10))
        self.consumables.append(ConsumableHealingItem("Greater Health Potion",
                                                      "A mystical potion that heals for 30 health.", 10, 1, 30))
        self.consumables.append(ConsumableHealingItem("Superior Health Potion", "This potion is brewed from the blood of the gods It is rumored that those who drink from it enough will achieve eternal life.",
                                                      10, 1, 100))

    def getConsumable(self, position):
        return self.consumables[position]

ConsumableItems(0)