# Day 10: Calculator
from os import system


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


symbols = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():

    should_continue = True
    num1 = float(input("Enter first number:\n"))
    while should_continue:
        num2 = float(input("\nWhat's the next number:\n"))
        print()
        for symbol in symbols:
            print(f"{symbol}  ", end="")
        operation = input("\n\nSelect an operation from the list above:\n")
        calc_function = symbols[operation]
        answer = calc_function(num1, num2)
        print(f"\n{num1} {operation} {num2} = {answer}")
        choice = input(f"\nType 'C' to continue calculating with {answer} or 'F' to start a new calculation: \n").lower()
        if choice == "c":
            num1 = answer
        else:
            system("clear")
            calculator()


calculator()
