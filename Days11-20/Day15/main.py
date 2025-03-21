from os import system
from time import sleep
from menu import MENU

espresso_cost = MENU["espresso"]["cost"]
latte_cost = MENU["latte"]["cost"]
cappuccino_cost = MENU["cappuccino"]["cost"]
profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def greet():
    system("clear")
    print("Welcome to Barista Coffee")
    print("\n\t     MENU")
    print(f"* Espresso\t\t ${espresso_cost}")
    print(f"* Latte\t\t\t ${latte_cost}")
    print(f"* Cappuccino\t\t ${cappuccino_cost}")


def print_report():
    system("clear")
    sleep(0.5)
    print("Resources remaining\n")
    print(f"* Water: \t{resources['water']}mL")
    print(f"* Milk: \t{resources['milk']}mL")
    print(f"* Coffee: \t{resources['coffee']}g")
    print(f"* Money: \t$ {profit}")


def is_resource_sufficient(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print(f"\n⚠️ Sorry there is not sufficient {item}")
            return False
    return True


def process_coins():
    print("\nPlease insert coins 🔽")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total


def is_transaction_successful(payment, drink_cost):
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        print(f"\nHere's your ${change} change & ", end="")
        return True
    else:
        print("SORRY! that's not enough money. Money refunded.")
        return False


def make_coffee(drink):
    drink_ingredients = MENU[drink]["ingredients"]
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"your {drink}. ENJOY ☕️")


def coffee_maker():
    greet()
    order = input("\nWhat would you like to drink:\n").lower()
    if order == "report":
        print_report()
    elif order == "off":
        print("\nTurning OFF the machine ⚠️")
        sleep(2.5)
        print("Machine turned OFF 😴")
    else:
        drink = MENU[order]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                global profit
                profit += drink["cost"]
                make_coffee(order)


coffee_maker()
