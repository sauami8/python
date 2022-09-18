"""

def a_decorator(fun):
    print("Hello Main function")
    n="this is it"
    def wrapper_b(a,b):
        c = a+b
        n1=n+" Thanks"
        return fun(c,n1)
    return wrapper_b

@a_decorator
def mydec(a,b):
    print("hello name is  ",a,b)

mydec(1,2)

"""
class decorator_class(object):
    print("Class decorator print as soon as @called with function")
    def __init__(self, push_function):
        self.push_function = push_function

    def __call__(self, *args, **kwargs):
        print("Calling wrapper function which takes param for function: {} ".format(self.push_function.__name__))
        print(f"Argument of {args} and values are {kwargs}")
        return self.push_function(*args, **kwargs)

@decorator_class
def say_hello():
    print("Hello Class {}".format(__name__))



@decorator_class
def hello_class_func(a,b):
    """annotation"""
    print("Hello -->{}<-- , this is -->{} <--decorator {}".format(a,b,__name__))

hello_class_func("Tom","Class")
# print("\n\n\n")
#say_hello()

def say_hello():
    print("\n\nsay Hello ".format(__name__))
    #return func(x)
    small_hello()


def small_hello():
    print("Small Hello  123".__name__)

say_hello()