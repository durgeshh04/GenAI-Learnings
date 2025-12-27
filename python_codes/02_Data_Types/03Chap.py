# This file showcase the learnings of integer datatype and operators

# We import third party packages using import in python
import math

class Operations:
# def is a syntax for defining function in python
    def takeInputs(self, n):
        if n != 6:
            a = float(input("Enter first no: "))
            b = float(input("Enter second no: "))
            return a, b
        else:
            a = float(input("Enter value to check the value type (even or odd): "))
            return a

    def addition(self, a, b):
        print(f"Addition: {a + b}")

    def substraction(self, a, b):
        print(f"Substraction: {a - b}");

    def multiplication(self, a, b):
        print(f"Multiplication: {a * b}")

    def division(self, a, b):
        res = a / b
        print(f"Division: {res}")
        print(f"Ceil Division: {math.ceil(res)}")

    def floorDivision(self, a, b):
        print(f"Floor Division: {a // b}")

    def power(self, a, b):
        res = round(a ** b, 1)
        print(f"{a} to the power of {b} is {res}")

    
    def findEvenOrOdd(self, a):
        if a % 2 == 0:
            print(f"{a} is even value")
        else:
            print(f"{a} is odd value")


# input() function is used in python for taking user inputs
n = int(input("Enter any value in range of 1 to 7 to perform operation: "))


obj = Operations()

# match is like a switch in other programming languages
match n:
    case 1: 
        a, b = obj.takeInputs(n)
        obj.addition(a , b)
    case 2: 
        a, b = obj.takeInputs(n)
        obj.substraction(a, b)
    case 3: 
        a, b = obj.takeInputs(n)
        obj.multiplication(a, b)
    case 4: 
        a, b = obj.takeInputs(n)
        obj.division(a, b)
    case 5: 
        a, b = obj.takeInputs(n)
        obj.floorDivision(a, b)
    case 6:
        a, b = obj.takeInputs(n)
        obj.findEvenOrOdd(a)
    case 7: 
        a, b = obj.takeInputs(n)
        obj.power(a, b)
    case _:
        print("Invalid case")


# In python we can also store integers like this one:

# no = 10_00_000
# print(no)   # 1000000