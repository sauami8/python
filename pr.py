"""
import random

rand_val = random.randint(0,9)
l =[]

while rand_val != 9:

    rand_val = random.randint(0,50)
    try:
        assert rand_val ==8, "Value is not equal to 8"
        print("Value is: ", rand_val)
        l.append(rand_val)
    except AssertionError as assertion_msg:
        print("Assert message is : ",assertion_msg, "and randomm value is: ", rand_val)
        l.append(rand_val)
    print("total values evaluated: ", len(l), l)

tot_val = len(l)
print(l, end="----")
print("total values are evaluated--", tot_val)

if 50 in l:
    print("47 in l")

# run from cmd -- python3 /Users/sauami/Documents/Python/tmp/pr.py


d = {"a":"Apple", "b":"Boy"}

#d["a"]="value of aA"
#print(d["a"])
#print(d)
for k,v in d.items():
    print("dict key ",k, " value is ", v)
    if d[k] =="boy":
        print("chk conditiono Boy")
    else:
        print("No matching values")

d=[1,2,3]
if type(d) is dict:
    print("Object is dictionary")
elif type(d) is list:
    print("object is list")

print("---")
obj = {"ename":["a","b","c"], "id":[10,20,30], "city":{"Address":["coppell","TX"], "Country":"US"}}
print(obj," is type of ",type(obj),"\n")
for k, v in obj.items():
    if type(v) is list:
        print(k, "is key type of list ", v)
        for vname in v:
            print("\tValue of Key ", k, " are ", vname)
    elif type(v) is dict:
        print(k, "<- type of dict-> ", v)
        for k1,v1 in v.items():
            print("\t", k1, "Nested value Key")
            if type(v1) is list:
                for v1v in v1:
                    print("\t\tVales are ", v1v)
            if type(v1) is str:
                print("\t\tvalue is str", v1)
    elif type(v) is str:
        print("\tKey is string ", k, " and value is ", v)
    elif type(v) is int:
        print("\tKey is int ", k, " and value is ", v)
    else:
        print("value is different ", v)
"""
a = "hello"
b="Jai %s"
print(b%a)

a= True
if bool(a):
    print('t')
else:
    print("false")

mylam = lambda a,b: a**b
print(mylam(3,3))

import pandas as pd

a = [a,2,3,4,5,6]
ps = pd.Series(a)
print(ps)