from EnemyBasic import EnemyBasic
from ConsumableHealingItem import ConsumableHealingItem
import ConsumableItemsList

ListofEnemies = []

# -----------------------------------------Chad enemy loot table and enemy is created. Enemy 0.
# Enemy Class template (Name, Description, level, playerlevel, hp, exp, damage, lootTables, icon).

ChadsLoot = [ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0]]
Chad = EnemyBasic("Chad", "Boring", 1, 1, 30, 50, 2, ChadsLoot, 'chad')
ListofEnemies.append(Chad)

BazingaLoot = [ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[0], ConsumableItemsList.consumables[1], ConsumableItemsList.consumables[1]]
Bazinga = EnemyBasic("Sheldon", "Beware of the Bazinga.", 2, 1, 40, 50, 3, BazingaLoot, 'sheldon.png')
ListofEnemies.append(Bazinga)