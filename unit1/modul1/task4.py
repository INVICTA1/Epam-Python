import math

num = float(input('Enter number:'))


def calculate(num):
    whole = math.trunc(num)
    fractional = num - whole
    value = whole / 1000 + fractional * 1000
    return value


print("result", calculate(num))
