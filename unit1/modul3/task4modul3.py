def calculate():
    i = 1
    sum = 1

    for i in range(1, 200):
        sum *= i ** 2
        i += 1
    return sum


print('answer:', calculate())
