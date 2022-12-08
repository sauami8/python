
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
        

for i in range(1,10):
    if i==3:
        continue
    else:
        print('numner is ',i)


while True:
    try:
        a = input("Enter number: ")
        a = int(a)
        print("number squar is", a**a)
        
    except:
        print('not a number')
        break