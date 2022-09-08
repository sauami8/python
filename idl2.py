
#list Compheransive
my_list = [1,2,3,4,5,6,7,8,9,0]
sqr_list = [ new_list**2 for new_list in my_list]
sqr_list
[1, 4, 9, 16, 25, 36, 49, 64, 81, 0]

sqr_list = [ new_list*new_list for new_list in my_list]
>>>sqr_list
>>>[1, 4, 9, 16, 25, 36, 49, 64, 81, 0]

#Generator
def sqr_gen(num):
    for i in num:
        yield (i*i)
        
my_gen = sqr_gen(my_list)

print(next(my_gen))
#you can get genrator value from for loop
for x in my_gen:
    print(x)




def add_num(my_func,v2):
    return my_func+v2+1

def arg_func(ret_fun):
    mynum = 345
    mynum2 = 4
    return ret_fun(mynum, mynum2)

print(add_num(1,1))

#Here arg_func taking function as parameter and returning the calling funciton with value that will used in passing func
#in this case add_num passed as argument and within regurn call is made to this function with value MYNUM variable
print(arg_func(add_num))

#lambda

def lam(x):
    import random
    r= random.randint(0,78)
    print("random num is: ",r)
    print("input num is: ",x)
    return lambda l: x+r+l

#lam function is loaded to m and wating for lambda to execute which is called with m(20) by passing 20 as value for lambda l
m= lam(2)
random num is:  24
input num is:  2

m(20)
>>>46

#Class Decorator

class decorator_class(object):
    def __init__(self, push_function):
        self.push_function = push_function

    def __call__(self, *args, **kwargs):
        print("Calling wrapper function which takes param for function: {} ".format(self.push_function.__name__))
        print(f"Argument of {args} and values are {kwargs}")
        return self.push_function(*args, **kwargs)

@decorator_class
def say_hello():
    print("Hello Class {}".format(__name__))

say_hello()

@decorator_class
def hello_class_func(a,b):
    print("Hello {} , this is {} decorator ".format(a,b))

hello_class_func("Tom","Class")



'''
#to handle different numbers of function parameter scenrio python use *args and **kwargs
#that basically passed to wrapper function and same is used in calling function 


def my_decorator_func(anyfunc):
    print("-- this is decorator function applying on calling function - {0}".format(__name__))
    def wrapper_func(*args, **kwargs):
        print("\tthis is Wrapper Function - {} ".format(wrapper_func.__name__))
        return anyfunc(*args, **kwargs)
    return wrapper_func

@my_decorator_func
def hello():
    print("\t\tHello World function is {} ".format(hello.__name__))

hello()
print("\n\n\n")

##Step1 at this moment only my_decorator_fun will execute and keep waiting for wrapper_fun to execute with will execute with steps 2
@my_decorator_func
def say_hello(n,age):
    print("\t\tHello Mr {} your age is {} func name {}".format(n,age,say_hello.__name__))

##Step 2 calling the wrapper function which inturn called say_hello    
say_hello("John",30)

print("\n\n\n")
##This is traditional way to call a function
##h = hello()
##h
##h1 = say_hello("Jhon",25)
##h1
   


def ht_tag(tag):
    def wrap_tag(msg):
        print(f"<{tag}>{msg}</{tag}>")
        print("<{0}>{1}</{0}>".format(tag,msg))
    return wrap_tag

h = ht_tag("H1")
h("Hello World")

h= = ht_tag("H2")
h("Beautiful Day !")


def cube(x):
    return x*x*x

def sqr(x):
    return x*x

def fun_tbl(myfunc, mlist):
    l = []
    for i in mlist:
        l.append(myfunc(i))
    return l

c = fun_tbl(cube, [1,2,3,4])
print(c)

c1 = fun_tbl(sqr, [1,2,3,4])
print(c1)



#Decorator basic level 1
def decorator_func(my_func):

    def wrapper_func():
        return my_func()

    return wrapper_func


def say_hello():
    print("Level 1 - This is example of Python Decorator:")

decorator_disp = decorator_func(say_hello)
decorator_disp()


#Decorator basic level 2 using decorator keyword
def decorator_func(my_func):
    print("\t Decorator execution 1 - this is main decoractor")
    
    def wrapper_func():
        print("\t\tRunning this before wrapper {} ".format(my_func.__name__))
        print("\t\tWrapperFunc  join decorator")
        
        return my_func()

    return wrapper_func

@decorator_func
def say_hello():
    print("Level 2 - This is example of Python Decorator:")

#calling decorated function    
say_hello()
# this part is not needed when using @decorator -- decorator_disp = decorator_func(say_hello)
#decorator_disp()


#3
print("------------ 3--------")
def deco(func2):
    x=10
    def myfunc(a):
        print(f"this is my function two and x is {x} and")
        return func2(a) #you can pass x in this case out would be 50 for a output 10
    return myfunc

@deco
def cal(a):
    print("#3", a*5)
    #return 

cal(2)

#4th way of using decorator
def my_dec(a):
    x="Beautiful day"
    return a(x)

@my_dec
def h(a):
    print(f"hello #4 {a}")
#calling h function
h

#Passing function as agrument and using the Python first class functionality by using parameter as argument
def per(p):
    ad = float(input("Enter the additional discount to apply"))
    print("Final Price after Discount: ",p - (p*(ad/100)))
    return p*(ad/100)

def dis(d):
    amount =float(input("Enter the Amount: "))
    discount =float(input("Enter the Discount: "))
    x= amount - ((amount*discount)/100)
    print("Discounted amount is :" , x)
    return d(x)

#lp = dis(per)
#print(lp)
print("Your additional discount is: " , dis(per))


def my_lam(a,b):
    x = lambda a,b: (a/b)
    v = x(a,b)
    print(v)
    return v



my_lam(6,2)



def say_hello():
    return "Hello Wrold"

fa = say_hello
print("function assign to FA variable ",fa)

fc = say_hello ()
print("Function called and variable FC store the value ",fc)




def out_func(msg):
    message = msg

    def inner_func():
        print(message)
    return inner_func

# when outer func is execute it return the inner func which is waiting to be execute
#if inner function retun like inner_func(), which is function execute 
v=out_func("Hello")
v()
#>>> function out_func.<locals>.inner_func at 0x1078da950>
#outer function sending inner function to v_in variable and next line inner function is execyted

v_by = out_func("Bye")
v_by()

#2nd way to return executed function not require to execute inner func with the help of variable
def out_func(msg):
    message = msg

    def inner_func():
        print(message)
    return inner_func()

out_func("Hi")
out_func("Bye")

#3way to remove the middle variable and directly pass the variable to inner func

#2nd way to return executed function not require to execute inner func with the help of variable
def out_func(msg):
    #message = msg

    def inner_func():
        print(msg)
    return inner_func()

out_func("Good")
out_func("Morning")


'''
