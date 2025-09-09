from collections import Counter

inventory = Counter()
loot = {"xp": 1000, "gold": 200, "potion": 4}
inventory.update(loot)
print(inventory)

inventory.update({"gold": -100, "potion": 1, "elixir": 3})
print(inventory)
