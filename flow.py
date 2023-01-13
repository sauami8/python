def funca(x):
    if x==1:
        print("hello")
        v=x
    else:
        v = x+1
    print(f'main function funca value pass{x} and function outcome {v}')
    def infunc(v):
        print(f'Value of inFunc is {v} ')
        if v==2:
            x1=100
        else:
            x1=200
        return x1
    return infunc


def ff():
    print("FF func")

r = funca(2)
print(f'-------\n')
print(r(2))
print(f'-------\n')

if r(1) == 100:
    print("no prob")
# else:
    # exit() # this will stop the execution going forward so no futher code execution



ff()


def my_func2():
    print("hello world")

my_func2()