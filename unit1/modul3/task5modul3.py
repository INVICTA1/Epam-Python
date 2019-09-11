import math

e = float(input('enter e'))
n = 1
a = 1 / 2 ** n + 1 / 3 ** n
sum = 0
while math.fabs(a) > e:
    a = 1 / 2 ** n + 1 / 3 ** n
    sum += a
    n += 1
print('sum:', sum)
