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

x = add_num

y = arg_func(x)
print(x.__name__, y)