a = int(input('enter a'))
b = int(input('enter b'))
h = int(input('enter h'))
x = a
for x in range(a, b + 1, h):
    if x > 2:
        y = x
    else:
        y = -x
    print("y=", y)

