class Pet:
    def __init__(self, name, money, inventory, health, sanity, hunger, thirst, energy, happiness):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.health = health
        self.sanity = sanity
        self.hunger = hunger
        self.thirst = thirst
        self.energy = energy
        self.happiness = happiness
    
    def buy(self, item):
        cost = item["cost"]
        print ("do you want to buy?")
        if input == ("yes, yep, yea, yeah").lower:
            if self.money >= cost:
                self.money -= cost
            self.inventory.append(item)
            print("u bought:", item)
            print("heres your updated inventory:", self.inventory)
            print("your money left:", self.money)
        elif input ==("no, nah, nuh uh").lower:
                print ("okay bye bye")
        else:
            print("ur too poor need more money", item["title"])
dolphin = Pet("dolphin", 167, ["fish"], 100, 100, 100, 100, 100, 67)
item = {"title": "t-90m", "cost": 67}
dolphin.buy(item)
print(dolphin.__dict__)
