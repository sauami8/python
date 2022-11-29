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
    print('Try Else Block - x is equal or higher then 5')
finally:
    print('Try and except block is complete, and this will exeute no matter whether block raised error or')