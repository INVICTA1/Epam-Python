import math

e = float(input('enter e'))


def calculate(e):
    sum = 0
    n = 1
    a = 1 / 2 ** n + 1 / 3 ** n

    while math.fabs(a) > e:
        a = 1 / 2 ** n + 1 / 3 ** n
        sum += a
        n += 1
    return sum


print('sum:', calculate(e))
