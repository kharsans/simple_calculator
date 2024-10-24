"""This module contains the calculator functions for the formulas square, tri, lazy caterer, and magic squares"""

import math 

def squareNums(n):
    """Calculates the square"""
    return n**2


def triNums(n):
    """Calculates the tri number"""
    return (n * (n + 1)) / 2


def lazyCaterer(n):
    """Calculates the lazy caterer number"""
    return (n**2 + n + 2) / 2


def magicSquares(n):
    """Calculates the magic squares number"""
    return (n * (n**2 + 1)) / 2

"""my three calculator are here after this comment"""

def calculatehypotenuse(a, b):
    """Calculates hypotenuse"""
    return math.sqrt(a**2 + b**2)


def volumeOfSphere(radius):
    """Calculates volume of sphere when """
    return (4/3) * math.pi * (radius ** 3)
    
    
def celsiusToFahrenheit(celsius):
    return (celsius * 9/5) + 32
    

def run_calculator(input_formula, input_num):
    """Calls and returns results for the specified formulas"""
    calculator = [squareNums, triNums, lazyCaterer, magicSquares]
    formula = calculator[input_formula - 1]
    return_result = formula(input_num)
    return return_result


if __name__ == "__main__":
    print(
        "Choose which formula to use: 1 for square, 2 for tri, 3 for lazy caterer, 4 for magic squares, 5 for calculate hypotenuse,, 6 for volume of sphere, 7 for celcius to farheinheit"
    )
    input_formula = int(input())
    print(
        "Enter a number to calculate the square, tri, lazy caterer, and magic squares numbers"
    )
    input_num = int(input())

    result = run_calculator(input_formula, input_num)
    print(result)
