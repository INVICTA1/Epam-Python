import math

x = int(input('Enter x:'))
y = int(input('Enter y:'))


def calculate(x, y):
    return (math.sin(x) + math.cos(y)) / (math.cos(x) - math.sin(y)) * math.tan(x * y)


print("result", calculate(x, y))
