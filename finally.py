# finally with try and except

import random
x1 = random.randint(1,10)
# x = random.randint(1,10)
print('Value of X1 ')
try:
    x > 5 
    print('In TRY -> x is ')
except:
    print('Except Block')
else:
    print('Try Else Block - This Block will execute with Try, will not execute in case of exception')
finally:
    print('Try and except block is complete, and this will exeute no matter whether block raised error or not')
    print('Most important -> This can be useful to close objects and clean up resources')