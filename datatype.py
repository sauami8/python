# a = input('Enter the object value ==> ')
a=True
while True:
    try:
        type(a) == int
        if type(a)==int:
            print('Input type is Integer')
        elif type(a)==bool:
            print('Input type is  bool')
        elif type(a)==str:
            print('Input type is  string')
        elif type(a)==list:
            print('Input type is its list')
        else:
            print('something new, lets research')
        break
    except:
        print('something else Try again')
        