def calculate():
    i = 1
    sum = 0
    for i in range(1, 100):
        sum += i ** 2
        i += 1
    return sum


print('Sum:', calculate())
