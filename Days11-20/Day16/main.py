# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# # Aligning table contents
# table.align = "l"
# print(table)

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system
from time import sleep

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


def start_machine():
    system('clear')
    print("WELCOME TO BARISTA COFFEE")
    print(f"\n{menu.get_items()}")
    order = input(f"What would you like to have?\n")
    if order == "off":
        print("⚠️  Turning OFF the machine  ⚠️")
        return
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
            sleep(3)


start_machine()
