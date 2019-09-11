def calculate(x, y):
    if x < y:
        return x
    else:
        return y


a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))
d = int(input('Enter d:'))
if calculate(a, b) > calculate(c, d):
    max = calculate(a, b)
else:
    max = calculate(c, d)
print("max:", max)
