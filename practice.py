# define variables
reversal = 0
# interactive input
pal = int(input('Enter a Number '))
tempe = pal
# computation/compare
while(pal>0):
    dig = pal % 10
    reversal = reversal*10+dig
    pal = pal//10


# report result
if(tempe==reversal):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")


"""
def deco2(func):
    print("Inner Decorator Func name -> {}".format(func.__name__))
    def two_wrap(a,b):
        print("\tinner Wrapper func -> {}".format(func.__name__))
        a=a
        b= b*10
        return func(a,b)
    return two_wrap

def main_deco(func):
    print("\nThis is Outer Decorator function name > {} ".format(__name__))

    def deco_wrapper (a,b):
        print("\tOuter Wrapper Decorator > {}".format(func.__name__))
        a= a
        b=b*2
        return func(a,b)
    return deco_wrapper

@main_deco
@deco2
def add_num(a,b):
    print(f"Final function Adding Number value function name {a},{b} ")
#Till here Decorator\'s loaded into memory 
add_num(2,4)


def a ():
    x="hello"
    c="no match"
    assert(x=="helo"),c
    return c
    

print(a())



class Employee:
    increment = 1.05
    cnt = 0    
    def __init__(self, fname, lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'
        Employee.cnt +=1

    def full_name(self):
        return "{} {}".format(self.fname,self.lname)

    def raise_amt(self):
        self.pay = int(self.pay * self.increment)

e1 = Employee("sr", "Raj",100)

print(e1.email, e1.pay)
e1.raise_amt()

print(e1.email, e1.pay)

class emp:
    increment = 1.05
    cnt = 0

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname+lname+'@instance.com'
        emp.cnt+=1

    #this method works same as creating new instance for class but require some sort of additional task to get class arguments

    @classmethod
    def add_new_emp(cls, mystr):
        fname, lname, pay = mystr.split("-")
        return cls(fname, lname,pay) 

#Static method don't take neither class or instance parameter automatically but it has logical linking/relation with class
    #@staticmethod 
    def from_age(age):
        d = 365
        return float((age*d)+emp.increment)

age2day = emp.from_age(10)
print("Total number of days in age is ", age2day)

cdata = 'saurabh-raj-888'

ne = emp.add_new_emp(cdata)

print(type(ne))
print(f"New emp {ne.email} added and pay is {ne.pay}")
"""