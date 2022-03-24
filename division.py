import math

def get_input():
    print("the first number:")
    a = input()
    print("the second number:")
    b = input()
    return a, b

def division(a, b):
    if b != 0:
        result = float(a)/b
        return result
    else:
        print("denominator can't be zero!")

if __name__ == "__main__":
    a, b = get_input()
    answer = division(a, b)
    print("a / b = %f"%answer)
