
# calculator

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("Enter the first number: "))
    for operator in operations:
        print(operator)

    should_continue = True

    while should_continue:
        op_symbol = input("Pick an operation: ")
        num2 = float(input("Enter the next number: "))

        calculation = operations[op_symbol]
        answer = calculation(num1, num2)

        print(f"{num1} {op_symbol} {num2} = {answer}")

        if input("Do you want to continue? type 'y' for Yes or 'n' for No: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()