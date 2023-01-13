# #git token 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
# # require pandas and rdxl module to work with excel file

# import pandas as pd

# # variable to hold the excel file info

# file = pd.ExcelFile("sample_superstore.xls")

# #get excel sheet information

# print(f.sheet_names)

# # Variable will hold the excel file sheets info
# # to load the sheet data into pd dataframe variable need to parse for sheet in eg people sheet is used

# df = file.parse("People")

# print(df)

# # to access the specifix record from index
# df.loc[1]

# #to acccess the column values for dataframe
# df["Region"]

# #query multicolumn from df by index
# df.loc[1,"Person":"Region"]


# # check the records in dataframe based on column specific value
# # here df["Sales"] is Series which is directly query dataframe column values justlike >>>df["Sales"]
# #here we pass the series to DF location
# df.loc[df["Sales"]>=900]


# sheet.loc[sheet["Country"]=="United States"]

# #check DF any column values
# heet.Category   or  sheet.Country

# #check specific row and column values
# sheet.loc[1,"Quantity":"Profit"]

# #this will min sales amount from dataframe
# df.loc[df["Sales"].idxmin()]

# #this will return only country colunn value where sales amount is min in df

# df.loc[df["Sales"].idxmin()]["Country"]
# 'United States'
# df.loc[df["Sales"].idxmin()]["City"]
# 'Houston'

# #get unique info and can be use in for loop as well
# df.loc[df["Sales"]>10000]["Country"]
# 2623    United States
# 2697    United States
# 4190    United States
# 6826    United States
# 8153    United States
# Name: Country, dtype: object
# df.loc[df["Sales"]>10000]["Country"].unique()
# array(['United States'], dtype=object)
# df.loc[df["Sales"]>10000]["Country"].unique()

# for x in df.loc[df["Sales"]>10000]["Country"]:
#     print(x)

    
 

# United States
# United States
# United States
# United States

# #Set Custome index on DF to enable direct search on the column for specific values
# #here index set on "Category" field to search records for specific values
# sheet.set_index("Category", inplace=True)
# sheet.loc["Furniture"]

# #Reset the index
# sheet = sheet.reset_index(drop = True)

# #get the max discount
# pd["Discount"].max()
# #Two field values also be calculated as needed
# df.Sales.sum()
# 2297200.8603000003
# df.Sales.sum() - df.Discount.sum()
# 2295639.7703000004
# df.Discount.sum()
# 1561.09
# 2297200.8603000003-1561.09
# 2295639.7703000004

# #Highest sales entire record 
# df.loc[df["Sales"].idxmax()]
# #Highest sales customer info
# df.loc[df["Sales"].idxmax()]["Customer Name"]
# #>>>'Sean Miller

# #Get the unique Region values where Category is Furnicture
# df.loc[df["Category"]=="Furniture"]["Region"].unique()

# #You can create numpy array object from this
#   #type(region_date)
#    #<class 'numpy.ndarray'>
# region_date = df.loc[df["Category"]=="Furniture"]["Region"].unique()


# #Variable placeholder
# age=10
# name="Tom"
# a = "Hello %s and his age is %d"
# >>> a%(name,age)
# 'Hello Tom and his age is 10'


# #random code
# l = []

# for i in range(0,4):
#     f = input("Enter the List of Values to add: ").lower()
#     l.append(f)

# import random
# r = random.randint(0,4)
# lv = l[r]
# print("Value from list is: ",lv)

# while True:
#     ulv = input("Chooes the List value to match: ").lower()
#     if lv ==ulv:
#         print("you guessed it:", ulv)
#         break
#     else:
#         continue

# #nested function greetings
# def greetings():
#     def r_greet():
#         return "Hello World!"
#     return r_greet

# x = greetings()

# print(x())

# #Nested function

# def f1(a):
#     def f2(a):
#         return a+2
#     fv = f2(a)
#     return fv

# x = f1
# print(x(3))


# def s(a):
#     def s1(a):
#         return a*2
#     v = s1(a)
#     return v



# z = s(2)
# print(z)


# def msg(m):
#     "Main Func"
#     def sender(m):
#         return m
    
#     return print(sender(m))

# msg(1)

# def f1(a1):
#     def f2(a1):
#         return a1*2
#     fv = f2(a1)
#     return fv*2

# f = f1(2)
# print(f)

# #factorial
# def ft():
#     l = []
#     n = input("Enter for number for factorial: ")
#     for x in range(1,int(n)+1):
#         l.insert(0,x)
#     print(l)

# z =ft
# print(z())

# #pass statment - this use to crate empty block of code inside function body its like pl/sql package forward declaration 

# def myFunc():
#     pass

# #passing function as value looks like here 
# def f(b):
#     return b+2

# def f1(a):
#     x = 5 
#     return a(x)

# print(f1(f))


# #LAMBDA lambda
# def lmd(n):
#     x = lambda f: f*n
#     return x

# v = lmd(5)

# print(v(2))


# def my_lam(a,b):
#     x = lambda a,b: (a/b)
#     v = x(a,b)
#     print(v)
#     return v

# my_lam(2,2)


# #First class programming support all the feature or operation generally available to other entities, thease operaction
# #  typically includes being passed as an argument, return from a function and assign to a variable 
# def say_hello():
#     return "Hello Wrold"

# fa = say_hello
# print("function assign to FA variable ",fa)

# fc = say_hello ()
# print("Function called and variable FC store the value ",fc)
# >>>function assign to FA variable  <function say_hello at 0x104d4e440>
# >>>Function called and variable FC store the value  Hello Wrold




# def out_func(msg):
#     message = msg

#     def inner_func():
#         print(message)
#     return inner_func

# # when outer func is execute it return the inner func which is waiting to be execute
# #if inner function retun like inner_func(), which is function execute 
# v=out_func("Hello")
# v()
# #>>> function out_func.<locals>.inner_func at 0x1078da950>

# #outer function sending inner function to v_in variable and next line inner function is execyted

# v_bye = out_func("Bye")
# v_bye()

# #2nd way to return executed function not require to execute inner func with the help of variable
# def out_func(msg):
#     message = msg

#     def inner_func():
#         print(message)
#     return inner_func()

# out_func("Hi")
# out_func("Bye")

# #3way to remove the middle variable and directly pass the variable to inner func

# #2nd way to return executed function not require to execute inner func with the help of variable
# def out_func(msg):
#     #message = msg

#     def inner_func():
#         print(msg)
#     return inner_func()

# out_func("Good")
# out_func("Morning")



# #Passing function as agrument and using the Python first class functionality by using parameter as argument
# def per(p):
#     ad = float(input("Enter the additional discount to apply"))
#     print("Final Price after Discount: ",p - (p*(ad/100)))
#     return p*(ad/100)

# def dis(d):
#     amount =float(input("Enter the Amount: "))
#     discount =float(input("Enter the Discount: "))
#     x= amount - ((amount*discount)/100)
#     print("Discounted amount is :" , x)
#     return d(x)

# #lp = dis(per)
# #print(lp)
# print("Your additional discount is: " , dis(per))

# #------
# #Decorator in Python allow to add new functionality to the existing object without modifying its structure
# # #Object cound be Function, Method or a Class 

# # Structure of decorator function is

# def decorator_func(main_func):
#     def wrapper_func():
#         return main_func()
#     return wrapper_func


# #to handle different numbers of function parameter scenrio python use *args and **kwargs
# #that basically passed to wrapper function and same is used in calling function 


# def my_decorator_func(anyfunc):
#     print("-- this is decorator function applying on calling function - {0}".format(__name__))
#     def wrapper_func(*args, **kwargs):
#         print("\tthis is Wrapper Function - {} ".format(wrapper_func.__name__))
#         return anyfunc(*args, **kwargs)
#     return wrapper_func

# @my_decorator_func
# def hello():
#     print("\t\tHello World function is {} ".format(hello.__name__))

# hello()
# print("\n\n\n")

# ##Step1 at this moment only my_decorator_fun will execute and keep waiting for wrapper_fun to execute with will execute with steps 2
# @my_decorator_func
# def say_hello(n,age):
#     print("\t\tHello Mr {} your age is {} func name {}".format(n,age,say_hello.__name__))

# ##Step 2 calling the wrapper function which inturn called say_hello    
# say_hello("John",30)

# print("\n\n\n")
# ##This is traditional way to call a function
# ##h = hello()
# ##h
# ##h1 = say_hello("Jhon",25)
# ##h1
   
# #Class Decorator

# class decorator_class(object):
#     def __init__(self, push_function):
#         self.push_function = push_function

#     def __call__(self, *args, **kwargs):
#         print("Calling wrapper function which takes param for function: {} ".format(self.push_function.__name__))
#         return self.push_function(*args, **kwargs)

# @decorator_class
# def say_hello():
#     print("Hello Class {}".format(__name__))

# say_hello()

# @decorator_class
# def hello_class_func(a,b):
#     print("Hello {} , this is {} decorator ".format(a,b))

# hello_class_func("Tom","Class")

   

# #Decorator basic level 1
# def decorator_func(my_func):

#     def wrapper_func():
#         return my_func()

#     return wrapper_func


# def say_hello():
#     print("Level 1 - This is example of Python Decorator:")

# decorator_disp = decorator_func(say_hello)
# decorator_disp()


# #Decorator basic level 2 using decorator keyword
# def decorator_func(my_func):
#     print("\t Decorator execution 1 - this is main decoractor")
    
#     def wrapper_func():
#         print("\t\tRunning this before wrapper {} ".format(my_func.__name__))
#         print("\t\tWrapperFunc  join decorator")
        
#         return my_func()

#     return wrapper_func

# @decorator_func
# def say_hello():
#     print("Level 2 - This is example of Python Decorator:")

# #calling decorated function    
# say_hello()
# # this part is not needed when using @decorator -- decorator_disp = decorator_func(say_hello)
# #decorator_disp()

# #3
# print("------------ 3--------")
# def deco(func2):
#     x=10
#     def myfunc(a):
#         print(f"this is my function two and x is {x} and")
#         return func2(a) #you can pass x in this case out would be 50 for a output 10
#     return myfunc

# @deco
# def cal(a):
#     print("#3", a*5)
#     #return 

# cal(2)


# ============== RESTART: /Users/sauami/Documents/Python/tmp/idl2.py =============
# Level 1 - This is example of Python Decorator:
# 	 Decorator execution 1 - this is main decoractor
# 		Running this before wrapper say_hello 
# 		WrapperFunc  join decorator
# Level 2 - This is example of Python Decorator:
# ------------ 3--------
# this is my function two and x is 10 and
# #3 10

# output for x
# ============== RESTART: /Users/sauami/Documents/Python/tmp/idl2.py =============
# Level 1 - This is example of Python Decorator:
# 	 Decorator execution 1 - this is main decoractor
# 		Running this before wrapper say_hello 
# 		WrapperFunc  join decorator
# Level 2 - This is example of Python Decorator:
# ------------ 3--------
# this is my function two and x is 10 and
# #3 50


# #4th way of using decorator
# def my_dec(a):
#     x="Beautiful day"
#     return a(x)

# @my_dec
# def h(a):
#     print(f"hello #4 {a}")
# #calling h function
# h


# —Decorator with args and kwargs this allow to pass various number of parameter to execute different functions
# @wraps(orig_func)
#    def wrapper(*args, **kwargs):
#        logging.info(
#            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
#        return orig_func(*args, **kwargs)

#    return wrapper


# #Classess as Decorator


# #passing function to function 

# def cube(x):
#     return x*x*x

# def sqr(x):
#     return x*x

# def fun_tbl(myfunc, mlist):
#     l = []
#     for i in mlist:
#         l.append(myfunc(i))
#     return l

# c = fun_tbl(cube, [1,2,3,4])
# print(c)

# c1 = fun_tbl(sqr, [1,2,3,4])
# print(c1)

# #nested function with arguments
# def ht_tag(tag):
#     def wrap_tag(msg):
#         print(f"<{tag}>{msg}</{tag}>")
#         print("<{0}>{1}</{0}>".format(tag,msg))
#     return wrap_tag

# h = ht_tag("H1")
# h("Hello World")


# #Decorator with logging function
# # Decorators
# from functools import wraps


# def my_logger(orig_func):
#     import logging
#     logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

#     @wraps(orig_func)
#     def wrapper(*args, **kwargs):
#         logging.info(
#             'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
#         return orig_func(*args, **kwargs)

#     return wrapper


# def my_timer(orig_func):
#     import time

#     @wraps(orig_func)
#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         result = orig_func(*args, **kwargs)
#         t2 = time.time() - t1
#         print('{} ran in: {} sec'.format(orig_func.__name__, t2))
#         return result

#     return wrapper

# import time


# @my_logger
# @my_timer
# def display_info(name, age):
#     time.sleep(1)
#     print('display_info ran with arguments ({}, {})'.format(name, age))

# display_info('Tom', 22)
# #-------------------------

print('{} {}'.format(__name__, 'Hello'))



