from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system
from time import sleep

machineON = True

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

while machineON:
    system('clear')
    print("\t\t\tWELCOME TO MANAV'S CAFE\n")
    choice = input(f"What would you like to order ({menu.get_items()})\n").lower()

    if choice == 'off':
        sleep(1)
        print("\n\t\t\tMACHINE TURNED OFF")
        machineON = False
    
    elif choice == 'report':
        print("\n\t\t\tMACHINE REPORT")
        print("\t\t\t------- ------")
        coffeeMaker.report()
        moneyMachine.report()
        sleep(5)
    
    else:
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)
            
        sleep(3)