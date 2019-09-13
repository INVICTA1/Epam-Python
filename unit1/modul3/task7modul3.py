import math

m = int(input('enter m:'))
n = int(input('enter n:'))


def condition(m):
    for a in range(2, m):
        if m % a == 0:
            print(a)
        else:
            a += 1


def calculate(m, n):
    for m in range(m, n + 1):
        print("for number:", m, "dividers: ")
        condition(m)


calculate(m, n)
