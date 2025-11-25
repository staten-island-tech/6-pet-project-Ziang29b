class pet():
    def __init__(self, name, money, inventory, health, sanity, hunger, thrist, energy, happiness):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.health = health
        self.sanity = sanity
        self.hunger = hunger
        self.thrist= thrist
        self.energy= energy
        self.happiness= happiness
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
dolphin = pet("dolphin", 67, ["fish"], 100, 100, 100, 100, 100, 67)
dolphin.buy({"title": "Sword", "atk": 34} self.money-34)
print(dolphin.__dict__)
 