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
        price = item["price"]                    
        print("do you want to buy?")
        answer = input("do you want to buy? ").lower()

        if answer in ("yes", "yep", "yea", "yeah"):
            if self.money >= price:
                self.money -= price
                self.inventory.append(item)      
                print("u bought:", item)
                print("heres your updated inventory:", self.inventory)
                print("your money left:", self.money)
            else:
                print("ur too poor need more money", item)

        elif answer in ("no", "nah", "nuh uh").lower():
            print("okay bye bye")


dolphin = Pet("dolphin", 167, ["fish"], 100, 100, 100, 100, 100, 67)

stuff = [
    {
        "price": 2,                              
        "size": "about 3 inches",
        "name": "apple"
    },
    {
        "price": 2,                              
        "size": "6 or 7 inches",
        "name": "banana"
    },
    {
        "price": 222,                            
        "size": "10 feet long 1 feet 6 inches wide",
        "name": "giant baguette pillow"
    }
]

shopping = True

while shopping:
    user_input = input("what do you want, banana apple or giant baguette pillow: ").lower()

    found = False
    for item in stuff:
        if item["name"] == user_input:
            print(item)
            dolphin.buy(item)   
            found = True
            break

    if not found:
        print("we no have")

    user_input = input("are you still shopping? ").lower()
    if user_input in ["yea", "yes", "yeah", "yep", "yuh"].lower():
        print("okay enjoy your shopping")
    else:
        print("cashier is up front")
        break

print(dolphin.__dict__)

