def funca(x):
    if x==1:
        print("hello")
        v=x
    else:
        v = x+1
    def infunc(v):
        if v==2:
            x1=100
        else:
            x1=200
        return x1
    return infunc


def ff():
    print("FF func")

r = funca(1)
print(r(2))


if r(1) == 100:
    print("no prob")
else:
    exit()



ff()


def my_func2():
    print("hello world")

my_func2()