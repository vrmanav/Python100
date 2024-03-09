class CoffeeMaker:
    """Models the machine that makes the coffee"""

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"\t\t\tWater: {self.resources['water']}ml")
        print(f"\t\t\tMilk: {self.resources['milk']}ml")
        print(f"\t\t\tCoffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"\nSorry there is not enough {item}.", end='')
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"\nHere is your {order.name} ☕️. Enjoy!")
