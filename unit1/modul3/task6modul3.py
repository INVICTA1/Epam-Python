a = 0
while a != 'quit':
    try:
        letter = input('enter letter:')
        print("letter", letter, "=", ord(letter),"on code ASCII")
    except:
        print("enter data is'nt false")
    print("if you want to quit write 'quit'")
    a = letter
