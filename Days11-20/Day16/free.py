from os import system
from time import sleep

BALANCE = 0


def deposit_money():
    amount = 0
    add_cash = "yes"
    while add_cash == "yes":
        amount += int(input("\nHow many notes of ₹100: ")) * 100
        amount += int(input("How many notes of ₹200: ")) * 200
        amount += int(input("How many notes of ₹500: ")) * 500
        amount += int(input("How many notes of ₹2000: ")) * 2000
        add_cash = input(
            f"Total ₹{amount} deposited. Do you want to add more cash? [YES/NO]\n"
        )
    global BALANCE
    BALANCE = amount


def withdraw_money():
    amount = 0
    remove_cash = "yes"
    global BALANCE
    while remove_cash == "yes":
        amount = int(input("How much money would you like to withdraw?\n₹"))
        if amount < BALANCE:
            BALANCE -= amount
            remove_cash = input(
                f"₹{amount} debited. Do you want to add more cash? [YES/NO]\n"
            )
        else:
            print("⚠️ Insufficient balance ⚠️")


def view_balance():
    print(f"\nYour current balance is ₹{BALANCE}.")
    sleep(2)


def confirm_acc_number():
    acc_no_1 = int(input("\nEnter your account number:\n"))
    acc_no_2 = int(input("Confirm your account number:\n"))
    return acc_no_1 == acc_no_2


def show_menu():
    system("clear")
    print("Welcome to Crestwood Financial\n")
    print(f"\n* Deposit money")
    print(f"* Withdraw money")
    print(f"* View balance")
    print(f"* Exit")


def atm():
    exit_atm = False
    if confirm_acc_number():
        while not exit_atm:
            show_menu()
            operation = input("\nWhat would you like to do:\n").lower()
            if operation == "deposit money" or operation == "deposit":
                deposit_money()
            elif operation == "withdraw money" or operation == "withdraw":
                withdraw_money()
            elif operation == "view balance" or operation == "view":
                view_balance()
            else:
                print("\nThank you. See you soon! 👋🏼")
                exit_atm = True
                return
    else:
        print("\n⚠️  Account numbers do not match ⚠️")


atm()
