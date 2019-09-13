x = int(input('Enter x:'))
y = int(input('Enter y:'))
if x == 0 and y == -1:
    print("false")
elif -4 <= x <= 4:
    if -3 <= y <= 0:
        print("true")
    elif -2 <= x <= 2:
        if 0 <= y <= 4:
            print("true")
        else:
            print("false")
else:
    print("false")
