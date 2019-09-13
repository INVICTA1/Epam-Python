num = int(input('Enter num:'))


def calculate(num):
    sum = 0
    i = 1
    for i in range(1, num + 1):
        sum += i
        i += 1
    return sum


print("Sum:", calculate(num))
