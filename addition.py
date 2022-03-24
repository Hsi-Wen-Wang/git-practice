import numpy as np
import math

def add(a, b):
    sum = a + b
    return sum

def get_input():
    print("the first number is:")
    a = input()
    print("the second number is:")
    b = input()
    return a, b

if __name__ == "__main__":
    a, b = get_input()
    sum = add(a, b)
    print('a + b = %d'%sum)
