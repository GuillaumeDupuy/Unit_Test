class Calculator:

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y

    def power(x, y):
        result = 1
        for i in range(y):
            result *= x
        return result

    def square_root(x):
        if x == 0 or x == 1:
            return x
        val = x
        precision = 0.0000001
        while abs(val - x / val) > precision:
            val = (val + x / val) / 2
        return val

def calculate(operation, x, y):

    if operation == "add":
        result = Calculator.add(x,y)
    elif operation == "substract":
        result = Calculator.subtract(x,y)
    elif operation == "multiply":
        result = Calculator.multiply(x,y)
    elif operation == "divide":
        result = Calculator.divide(x,y)
    elif operation == "power":
        result = Calculator.power(x,y)
    elif operation == "square_root":
        result = Calculator.square_root(x)
    return result

operation = input("Enter the operation you would like to perform (add,subtract, multiply, divide, square_root, power): ")
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the secod number : "))

print(calculate(operation, num1, num2))