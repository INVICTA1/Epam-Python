import math
num=float(input('Enter number:'))
whole=math.trunc(num)
fractional=num-whole
value=whole/1000+fractional*1000
print(value)
