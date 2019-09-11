import math

time = int(input('Enter second'))
hours = int(time / 3600)
minutes = int((time - hours * 3600) / 60)
seconds = time - hours * 3600 - minutes * 60
print(hours, "ч", minutes, "мин", seconds, "с")
