from EnemyBasic import EnemyBasic
from ConsumableHealingItem import ConsumableHealingItem
import ConsumableItemsList

ListofEnemies = []

# -----------------------------------------Chad enemy loot table and enemy is created. Enemy 0.
ChadsLoot = [ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0]]
Chad = EnemyBasic("Chad", "Boring", 1, 1, 30, 50, 2, ChadsLoot, 'chad')
ListofEnemies.append(Chad)