from EnemyBasic import EnemyBasic
from ConsumableHealingItem import ConsumableHealingItem
import ConsumableItemsList

ListofEnemies = []

# -----------------------------------------Chad enemy loot table and enemy is created. Enemy 0.
ChadsLoot = [ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0]]
Chad = EnemyBasic("Chad", "Boring", 5, 5, 20, 50, 2, ChadsLoot)
ListofEnemies.append(Chad)