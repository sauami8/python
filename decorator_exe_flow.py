from functools import wraps



def md(func):
    #@wraps(func)
    def mw(a,b):
        a = a+2
        b +=2
        print("Exeecuting MW {}".format(func.__name__))
        return func(a,b)
    return mw


def sd(func):
    #@wraps(func)
    def sw(a,b):
        a /=3
        b/=3
        print("executing SW {}".format(func.__name__))
        return func(a,b)
    return sw

@sd
@md
def my_func(a,b):
    print(f"My Func a {a} and B {b} {__name__}")

my_func(2,2)

"""
one = md(my_func)
print("manual ",one)
one(1,1)

two = sd(md(my_func))
print("manual two",two)
two(1,1)

sauami@Sauami tmp % /usr/local/bin/python3 /Users/sauami/Documents/Python/tmp/decorator_exe_flow.py
manual  <function md.<locals>.mw at 0x1033a4820>
Exeecuting MW
My Func a 3 and B 3
manual two <function sd.<locals>.sw at 0x1033a4940>
executing SW
Exeecuting MW
My Func a 6 and B 6
sauami@Sauami tmp % 
"""

#theory here from two --this part -- md(my_func) -- is equal to mw and whole two is equal to sw
#first sd will execute which will call sw func 


"""
from functools import wraps

def deco2(func1):
    print("Inner Decorator Func name -> {}".format(func1.__name__))
    @wraps(func1)
    def two_wrap(a,b):
        print("\tinner Wrapper func -> {}".format(func1.__name__))
        a=3
        b= b*10
        print("Inner : ",a,b)
        return func1(a,b)
    return two_wrap

def main_deco(func2):
    print("This is Outer Decorator function name > {} ".format(func2.__name__))

    @wraps(func2)
    def deco_wrapper (a,b):
        print("\tOuter Wrapper Decorator > {}".format(func2.__name__))
        a= 5
        b=b*2
        print("Outer ", a,b)
        return func2(a,b)
    return deco_wrapper

@deco2
@main_deco
#@deco2
def add_num(a,b):
    print(f"Final function Adding Number value function name {a},{b}")
#Till here Decorator\'s loaded into memory 
add_num(2,4)

"""
