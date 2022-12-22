
# Basic decorator framework

def decorator(original_function):
    def wrapper_func():
        return original_function
    return wrapper_func


# Additional 10% discount decorator function
def add_dis(fun):
    def wrap(i,p):
        if i=='Book':
            p=p-(p*.1)
        elif i=='Laptop':
           p=p-(p*.2) 
        return fun(i,p)
    return wrap


@add_dis
def item_price(i,p):
    print(f'Product {i} price is {p}')
    # return p


item_price('Laptop',80)

