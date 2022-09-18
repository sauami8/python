from typing import List


def x(lv: List[float]):
    for i in lv:
        print(i)


x([1,2,3])



"""
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