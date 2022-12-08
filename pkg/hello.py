while True:
    try:
        n = input('Enter Your name: ')
        a = float(input('Enter your age: '))
        print(f"Your name is {n} and age is {a} ")
        break
    except:
        print('Enter your Age in numbers only ')
        c = input('Would you like to try again? (Y/N): ').upper()
        if c=='N':
            continue
        else:
            break