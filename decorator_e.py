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



def my_decorator_func(anyfunc):
   print("-- this is decorator function applying on calling function - {0}".format(__name__))
   def wrapper_func(*args, **kwargs):
       print("\tthis is Wrapper Function - {} ".format(wrapper_func.__name__))
       return anyfunc(*args, **kwargs)
   return wrapper_func

@my_decorator_func
def hello(a,b,c):
   print("Hello World function with values {}, {}, {} is {} ".format(a,b,c,hello.__name__))

hello(2,3,4)
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
