import numpy as np
import math

def get_input():
    print("the first number:")
    a = input()
    print("the second number:")
    b = input()
    return a, b

def subtraction(a, b):
    result = a - b
    return result

if __name__ == "__main__":
    a, b = get_input()
    answer = subtraction(a, b)
    print("a - b = %d"%answer)
