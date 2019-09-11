corner1 = int(input('Enter corner 1:'))
corner2 = int(input('Enter corner 2:'))
if corner1 + corner2 < 180:
    print('triangle is exist')
    if corner1 == 90 or corner2 == 90 or corner1 + corner2 == 90:
        print("triangle is rectangular")
    else:
        print("triangle is not rectangular")
else:
    print("triangle is not exist")
