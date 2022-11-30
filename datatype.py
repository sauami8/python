
# a=True
while True:
    try:
        a = float(input('Enter the object value ==> '))
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
            print('Type is not defined, lets research')
        break
    except:
        print('something else Try again')
        