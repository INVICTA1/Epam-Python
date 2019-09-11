import math
x=int(input('Enter x:'))
y=int(input('Enter y:'))
rezult=(math.sin(x)+math.cos(y))/(math.cos(x)-math.sin(y))*math.tan(x*y)
print(rezult)
