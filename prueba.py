import datetime
import os

def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

if __name__ == "__main__":
    print("Hola Mundo")
    print(suma(5,10))
    print(resta(10,5))
    print(multiplicacion(5,10))
    print(division(10,5))
    print(datetime.datetime.now())
    print(os.listdir())