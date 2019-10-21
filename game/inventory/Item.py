class Item:

    # All the important variables for a consumable item

    itemName: str = "XYZ"
    itemDescription: str = "XYZ"
    itemStackCap: int = 0
    itemStack: int = 0
    itemDropRate = 0

    # The constructor that sets the name, description, StackCap, Stack, and affect.
    def __init__(self, name, desc, stackCap, stack, dropRate):
        self.itemAffect(name, desc, stackCap, stack, dropRate)

    def itemAffect(self, name, desc, stackCap, stack, dropRate):
        self.setItemName(name)
        self.setItemDescription(desc)
        self.setItemStackCap(stackCap)
        self.setItemStack(stack)
        self.setItemDropRate(dropRate)

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

    # Most important function, setter and getter for drop rate.
    def setItemDropRate(self, rate):
        self.itemDropRate = float(rate)

    def getItemDropRate(self):
        return self.itemDropRate

class EquippableItem:
    itemName: str = "XYZ"
    itemDescription: str = "XYZ"
    levelReq = 0
    damage = 0

    def __init__(self, name, description, levelReq, damage):
        pass

    def setItemName(self, name):
        self.itemName = name

    def getItemName(self):
        return self.itemName

    def setItemDescription(self, desc):
        self.itemDescription = desc

    def getItemDescription(self):
        return self.itemDescription

    def setLevelReq(self, level):
        self.levelReq = level

    def getLevelReq(self):
        return self.levelReq

    def setDamage(self, damage):
        self.damage = damage

    def getDamage(self):
        return self.damage