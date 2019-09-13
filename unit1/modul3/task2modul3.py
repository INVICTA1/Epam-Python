a = int(input('enter a'))
b = int(input('enter b'))
h = int(input('enter h'))


def calculate(a, b, h):
    x = a
    for x in range(a, b + 1, h):
        if x > 2:
            return x
        else:
            return -x
    print("y=", calculate(a, b, h))
