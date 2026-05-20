import datetime
import os
import logging

logging.basicConfig(level=logging.INFO)

def suma(a,b):
    logging.info("Running suma")
    return a + b

def resta(a,b):
    logging.info("Running resta")
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    if b != 0:
        return a / b
    else:
        return "Error: division by zero"

if __name__ == "__main__":
    print("=== Calculator App ===")
    print(suma(5,10))
    print(resta(10,5))
    print(multiplicacion(5,10))
    print(division(10,5))
    print(datetime.datetime.now())
    print(os.listdir())