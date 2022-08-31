
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


'''
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
