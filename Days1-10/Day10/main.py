from os import system
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Storing a function inside a variable
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    system("clear")
    print("WELCOME TO MY CALCULATOR\n")
    n1 = float(input("Enter first number:\n"))

    do_continue = True

    while do_continue:
        print("Pick the operation you want to perform: ", end=" ")
        for symbol in operations:
            print(symbol, end=" ")
        operation = input("\n")
        n2 = float(input("Enter next number:\n"))
        answer = operations[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {answer}")

        choice = input(
            f"\nTo continue with {answer} type YES, to start fresh calculation type NEW, or to end type END:\n"
        ).lower()
        if choice == "end":
            do_continue = False
            print("\nGOOD-BYE 👋🏼")
        elif choice == "yes":
            n1 = answer
        else:
            calculator()


calculator()
