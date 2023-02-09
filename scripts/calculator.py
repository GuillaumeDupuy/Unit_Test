import math 

class Calculator:

    # def add(x, y): --> def add(self, x, y):
    def add(self, x, y):
        return x + y

    # def subtract(x, y): --> def subtract(self, x, y):
    def subtract(self, x, y):
        return x - y

    # def multiply(x, y): --> def multiply(self, x, y):
    def multiply(self, x, y):
        return x * y

    # def divide(x, y): --> def divide(self, x, y):
    def divide(self, x, y):
        return x / y

    # def power(x, y): --> def power(self, x, y):
    # Gérer le cas où y est négatif
    # Gérer le cas où x et y sont des flottants
    def power(self, x, y):
        # result = 1
        # for i in range(y):
        #     result *= x
        # return result
        
        # if y >= 0:
        #     result = 1
        #     for i in range(y):
        #         result *= x
        #     return result
        # else:
        #     return 1 / math.pow(x, -y)
        return x ** y

    # def square_root(x): --> def square_root(self, x):
    def square_root(self, x):
        if x == 0 or x == 1:
            return x
        val = x
        precision = 0.0000001
        while abs(val - x / val) > precision:
            val = (val + x / val) / 2
        return val

# Si on veut utiliser square_root, on a une erreur car on attend deux arguments alors qu'on a besoin que d'un seul
def calculate(operation, x, y=None):
    calc = Calculator()

    if operation == "square_root":
        result = calc.square_root(x)
    else:
        result = calc.__getattribute__(operation)(x, y)
    return result

# def calculate(operation, x, y):
#     # Création d'une instance de la classe Calculator
#     # Appeler la directement méthode de la classe Calculator
#     calc = Calculator()

#     if operation == "add":
#         # Calculator.add(x,y) --> calc.add(x,y)
#         result = calc.add(x,y)
#     elif operation == "substract":
#         # Calculator.subtract(x,y) --> calc.subtract(x,y)
#         result = calc.subtract(x,y)
#     elif operation == "multiply":
#         # Calculator.multiply(x,y) --> calc.multiply(x,y)
#         result = calc.multiply(x,y)
#     elif operation == "divide":
#         # Calculator.divide(x,y) --> calc.divide(x,y)
#         result = calc.divide(x,y)
#     elif operation == "power":
#         # Calculator.power(x,y) --> calc.power(x,y)
#         result = calc.power(x,y)
#     elif operation == "square_root":
#         # Calculator.square_root(x) --> calc.square_root(x)
#         result = calc.square_root(x)
#     return result

# operation = input("Enter the operation you would like to perform (add,subtract, multiply, divide, square_root, power): ")
# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the secod number : "))

# print(calculate(operation, num1, num2))