# import idl

# d = {'name':['Jhon','Dow','Tyler'], 'age':[10]}

# for k, v in d.items():
#     print('Key is: ', k)
#     for y in v:
#         print('values are: ', y)

import pandas as pd

s = pd.Series([10,12,14,15,18,36])
a=18
print("Series max value is --> ",s.max())
if s.max()==a:
    print("Series value is equal to variable")

# in range end number is exclusive

y = (x for x in range(1,40) if x < s.max())
y1 = [x for x in range(1,20) if x==s.max()]

print('value of y is: ', next(y))
for g in y:
    print('generator values:', next(y))
print("value From generator matching Series is --> ", sum(y))
print("Object Y is: ", y, " and Object Y1 is ", type(y1))

# pip install googletrans==3.1.0.0a0
from googletrans import Translator
t = "Hello Saurabh how are you today" #'''Hello world'''
trans = Translator()
out = trans.translate(t, dest="hi")
print(out.text)