import math

m = int(input('enter m:'))
n = int(input('enter n:'))
a = 1
for m in range(m, n + 1):
    print("for number:", m, " ")
    for a in range(1, m):
        if a != 1 and m % a == 0:
            print(a)
        else:
            a += 1
