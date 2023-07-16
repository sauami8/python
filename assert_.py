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