a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))


def calculate(a, b, c):
    return (b + (b ** 2 + 4 * a * c) ** (1 / 2)) / 2 * a - a ** 3 + b ** (-2)


print("result", calculate(a, b, c, ))
