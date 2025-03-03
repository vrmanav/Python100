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

print("WELCOME TO MY CALCULATOR\n")
n1 = float(input("Enter first number:\n"))
print("Pick the operation you want to perform: ", end=" ")
for symbol in operations:
    print(symbol, end=" ")
operation = input("\n")
n2 = float(input("Enter next number:\n"))
answer = f"{n1} {operation} {n2} = {operations[operation](n1, n2)}"
print(answer)
