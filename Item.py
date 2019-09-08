import math
import PlayerBase

class ConsumableItem:

    # All the important variables for a consumable item

    itemName: str = "XYZ"
    itemDescription: str = "XYZ"
    itemStackCap: int = 0
    itemStack: int = 0

    # The constructor that sets the name, description, StackCap, Stack, and affect.
    def __init__(self, arg1, arg2, arg3, arg4):
        self.itemAffect(arg1, arg2, arg3, arg4)

    def itemAffect(self, arg1, arg2, arg3, arg4):
        self.setItemName(arg1)
        self.setItemDescription(arg2)
        self.setItemStackCap(arg3)
        self.setItemStack(arg4)

    # The setter and Getter for itemName
    def setItemName(self, name):
        self.itemName = name

    def getItemName(self):
        return self.itemName

    # The setter and Getter for itemDescription
    def setItemDescription(self, desc):
        self.itemDescription = desc

    def getItemDescription(self):
        return self.itemDescription

    # Setters and Getters for itemStackCap and itemStack
    def setItemStackCap(self, cap):
        self.itemStackCap = cap

    def setItemStack(self, amount):
        self.itemStack = amount

    def getItemStackCap(self):
        return self.itemStackCap

    def getItemStack(self):
        return self.itemStack