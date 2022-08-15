import sys
from math import *

print("If you want to do raise to power of number use pow.\n" + "If you want to do square root use sqrt.\n" + "If you want to do factorial use fac.")

try:
    num1 = float(input("Enter the number: "))
except:
    print("This is not number")
    sys.exit()
op = input("Enter operator: ")

if op == "+" or op == "-" or op == "*" or op == "/" or op == "pow" or op == "sqrt" or op == "fac":
    if op == "sqrt":
        print(sqrt(num1))
    elif op == "fac":
        num1 = int(num1)
        print(factorial(num1))
    else:
        try:
            num2 = float(input("Enter the number: "))
        except:
            print("This is not number")
            sys.exit()
else:
    print("Invalid operator.")
    sys.exit()

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "pow":
    print(pow(num1 , num2))