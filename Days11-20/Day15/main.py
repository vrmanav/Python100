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


def print_report():
    system("clear")
    sleep(0.5)
    print("Resources remaining\n")
    print(f"* Water: \t{resources['water']}mL")
    print(f"* Milk: \t{resources['milk']}mL")
    print(f"* Coffee: \t{resources['coffee']}g")
    print(f"* Money: \t$ {profit}")


def greet():
    print("Welcome to Barista Coffee")
    print("\n\t     MENU")
    print(f"* Espresso\t\t ${espresso_cost}")
    print(f"* Latte\t\t\t ${latte_cost}")
    print(f"* Cappuccino\t\t ${cappuccino_cost}")


def is_resource_sufficient(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print(f"\n⚠️ Sorry there is not sufficient {item}")
            return False
    return True


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
            


coffee_maker()
