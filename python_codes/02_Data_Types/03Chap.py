def addition(a, b):
    print(a + b)

def substraction(a, b):
    print(a - b);

def multiplication(a, b):
    print(a * b)

def division(a, b):
    print(a / b)

def floorDivision(a, b):
    print(a // b)

n = int(input("Enter any value in range of 1 to 5 to perform operation: "))
a = 10
b = 5.5

match n:
    case 1: 
        addition(a , b)
    case 2: 
        substraction(a, b)
    case 3: 
        multiplication(a, b)
    case 4: 
        division(a, b)
    case 5: 
        floorDivision(a, b)
    case _:
        print("Invalid case")

