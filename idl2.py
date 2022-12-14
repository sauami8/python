#Print statment with END allow iterator item to be combine with as needed default is \n

l1 = [1 2 3 5]
for l in l1:
    print(l, end=",")

>>>1,2,3,5,

#Assert is like if condition

try:
    x = "OK"
    assert x == "O", "Value is not OK"
except AssertionError as assert_error_msg:
    print(assert_error_msg)

>>>Value is not OK


try:
    x = "OK"
    assert x == "OK", "Value is not OK"
    print("Value is checked and found Ok")
except AssertionError as assert_error_msg:
    print(assert_error_msg)

>>>Value is checked and found Ok


x = "hello"
assert x == "goodbye", "x should be 'hello'"
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    assert x == "goodbye", "x should be 'hello'"
AssertionError: x should be 'hello'

assert x == "hello", "x should be 'hello'"
>>no error here 

#Iterator - objects which are iterable can be used as iterator such as list, dictionary, tuppel etc
#method to create iterator
#Note: Iterator only go forward, not backword or resetting or making copy
itr_my_list = my_list.__iter__()

#or use the method in better way 
itr_my_list1 = iter(my_list)

itr_my_list
<list_iterator object at 0x107646620>
itr_my_list1
<list_iterator object at 0x107646b00>
#calling the iterator element from the list
next(itr_my_list1)
0
itr_my_list1.__next__()
9
itr_my_list1.__next__()
8
next(itr_my_list1)
7

#printing Iteration of list item
#Pseudo code- Iterable object like list (make list to Iterator by using iter method and then call the next element by using next method)


my_list = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13]
itr_my_list = my_list.__iter__()

while True:
    try:
        x=next(itr_my_list)
        print(x)
    except StopIteration:
        break


#list Compheransive
my_list = [1,2,3,4,5,6,7,8,9,0]
sqr_list = [ new_list**2 for new_list in my_list]
sqr_list
[1, 4, 9, 16, 25, 36, 49, 64, 81, 0]

sqr_list = [ new_list*new_list for new_list in my_list]
>>>sqr_list
>>>[1, 4, 9, 16, 25, 36, 49, 64, 81, 0]

#generator with list comp
x2 = (x+2 for x in [1,2,3,4,5])
                    
x2
                    
<generator object <genexpr> at 0x105308f20>

# for more clarity
#this will create list witih iteration
l = [x**2 for x in [1,2,3]]
                    
type(l)
                    
<class 'list'>

l = [x for x in range(0,10)]
                    
l
                    
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
type(l)
                    
<class 'list'>

l = [x for x in range(0,10)]                   
l             
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
type(l)                    
<class 'list'>

#but when used within squar brackets in this case it become ananymus block

l = (x for x in range(0,10))
                    
l
                    
<generator object <genexpr> at 0x105308f90>
next(l)
                    
0
for x in l:
    print(x)

                    
1
2
3
4
5
6
7
8
9

condition =True
x = 1 if condition else 0
x
1
condition =False
x = 1 if condition else 0
x
0

#comma seperator number in 
a=10_000
b=200_000
t = a+b
print(f"total is {t:,}")
total is 210,000
>>>total is 210,000


#Enum 
import enum
class ab(enum.Enum):
    A = 1
    B=2
    C=3
ab.A
<ab.A: 1>
print(ab.A, ab.B, ab.C)
ab.A ab.B ab.C
ab(1)
<ab.A: 1>
print(ab(1)
      )
ab.A
print(ab(2))
ab.B
ab.A
<ab.A: 1>
dir(ab.A)
['__class__', '__doc__', '__module__', 'name', 'value']


#List index and value from list start is optional default start with 0 enumerate gin-na
emp = ["jack","rose","Defney","Tom","Frank","Peter"]

for index, name in enumerate(emp , start=2):
    print(index, name)

    
2 jack
3 rose
4 Defney
5 Tom
6 Frank
7 Peter

#unpackig multiple list with zip

names = ["Spider man","Saktiman", 'Superman']
heros = ["Peter Parket", "Gangadhar", "Clark"]
company = ["Marvel","DD 1","DC Comic"]
for name, hero, comp in zip(names, heros, company):
    print(f"{name} - Played the role of \"{hero}\" and he is form \"{comp}\"")

    
Spider man - Played the role of "Peter Parket" and he is form "Marvel"
Saktiman - Played the role of "Gangadhar" and he is form "DD 1"
Superman - Played the role of "Clark" and he is form "DC Comic"


#Python Unit test assert are used 


#Generator note single integer value is not iterable because its single digit
def sqr_gen(num):
    for i in num:
        yield (i*i)
        
my_gen = sqr_gen(my_list)

print(next(my_gen))
#you can get genrator value from for loop
for x in my_gen:
    print(x)

#Generator with list compherensive

new_gen = [x*x for x in my_list]
print(new_gen)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 0]

#generator from list comprehnsive 
new_gen = (x*x for x in my_list)
new_gen
<generator object <genexpr> at 0x107676810>
for xx in new_gen:
    print(xx)

 >>>result is    
1
4
9
16
25
36
49
64
81
0


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

#random test 0 zero in python 0 in python is false
def test():
    a = [0,1, 4, 9, 16, 0]
    for x in a:
        if x==True:
            print("Value of x ",x)
        else:
            print("Value of X*x: ",x*x)

            
test()
Value of X*x:  0
Value of x  1
Value of X*x:  16
Value of X*x:  81
Value of X*x:  256
Value of X*x:  0

#list Comperhensive method
# test = [x*x for x in a if x]
test
[1, 16, 81, 256]


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

def a(fun):
    print("Hello Main function")
    n="this is it"
    def b(a,b):
        c = a+b
        n1=n+" Thanks"
        return fun(c,n1)
    return b

@a
def mydec(a,b):
    print("hello name is  ",a,b)

mydec(1,2)



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

# dictionary in list
d = [
 {
  "name":"Pen",
  "unit_price":5
 },
 {
  "name":"Eraser",
  "unit_price":3
 },
 {
  "name":"Pencil",
  "unit_price":10
 },
 {
  "name":"White paper",
  "unit_price":15
 }
]

for i in d:
    print(f"Accessing dict from list --> {i}")
    for x in i:
        print(f"Accessing dictionary key and values Key--> {x}, and Value --> {i[x]}")

        
Accessing dict from list --> {'name': 'Pen', 'unit_price': 5}
Accessing dictionary key and values Key--> name, and Value --> Pen
Accessing dictionary key and values Key--> unit_price, and Value --> 5
Accessing dict from list --> {'name': 'Eraser', 'unit_price': 3}
Accessing dictionary key and values Key--> name, and Value --> Eraser
Accessing dictionary key and values Key--> unit_price, and Value --> 3
Accessing dict from list --> {'name': 'Pencil', 'unit_price': 10}
Accessing dictionary key and values Key--> name, and Value --> Pencil
Accessing dictionary key and values Key--> unit_price, and Value --> 10
Accessing dict from list --> {'name': 'White paper', 'unit_price': 15}
Accessing dictionary key and values Key--> name, and Value --> White paper
Accessing dictionary key and values Key--> unit_price, and Value --> 15



#__name__ assign value __main__ to 