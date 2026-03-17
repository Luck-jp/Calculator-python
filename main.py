logo = """
 _____________________
|  _________________  |
| | Calc         0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

"""


def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    should_accumulate = True
    num1 = float(input("What is the first number:"))


    while should_accumulate:
        for symbol in operations: 
            print(symbol)
        operation_symbol = input("Pick an operation:")
        if operation_symbol not in operations:
            print("Invalid operation,Choose from the given options.")
            continue
        num2 = float(input("What is the next num:"))
        answer = operations[operation_symbol](num1, num2)
        rounded_answer = round(answer, 2)

        print(f"{num1} {operation_symbol} {num2} = {rounded_answer}")

        choice = input(f"Type 'y' to continue calculating with {rounded_answer}, or type 'n' to start a new calculation.").lower()

        if choice == "y":
            num1 = answer
        elif choice == "n":
            should_accumulate = False
            print("\n" * 20)
            calculator()
        else:
            print("Incorrect input. Choose 'y' or 'n'.")


calculator()
