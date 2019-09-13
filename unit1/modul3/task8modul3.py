num1 = input('enter number 1:')
num2 = input('enter number 2:')


def spisok(num1, num2):
    lis1 = list(num1)
    lis2 = list(num2)
    lis1.extend(lis2)
    lis1 = set(lis1)
    lis1 = list(lis1)
    lis1.sort()
    return lis1


print(spisok(num1, num2))
