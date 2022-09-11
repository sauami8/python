# empty class
from ast import increment_lineno


class emp:
    pass

#Class instace Class is simple blue print in this case e1 and e2 and both have different location in memory
e1 = emp()
e2 = emp()

print(e1)
print(e2)
# <__main__.emp object at 0x104a67f40>
# <__main__.emp object at 0x104a67f10>

class Employee:

    increment = 1.05
    cnt = 0
    #class variable can be access in fun with self self.increment or by referring Class.increment 5% increase
    #__init__ function call when instance is created and instance is passed in place of self without mentioning

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'
        Employee.cnt +=1

    def full_name(self):
        return "{} {}".format(self.fname,self.lname)

    def raise_amt(self):
        self.pay = int(self.pay * self.increment)


#create instance of the class with the value in the order defined in class init

e1 = Employee('saurabh', 'raj',100)
e2 = Employee("Hari","om",200)

print(e1.fname, e1.email)
print(e2.lname,e2.fname, e2.email)
print(e1)#this will tell that its object at memory location like <__main__.employee object at 0x1051fbeb0>

#Created the function to give full name now we can use the previously created instace of the class to get respected name
#let use both one after anohter
print("First instanace full name" , e1.full_name())
print("Full name from 2nd Instance", e2.full_name())

#we can directly use the class and method but in this case need to pass instance because full_name method take one parameter self which is instance

#before calling the raise_amt function to apply 5%
print(e2.__dict__)
print(e2.pay)

#e2.raise_amt()
print(Employee.full_name(e2))
#But in case of instance which have all parameters while creating instance and instance which have necessary parameter
# is passed to fullname func as self automatically

print(e2.full_name(), e2.pay, e1.pay)
#Increase after the raise_amt calculation pay is reset to new amount
print(e2.pay)

print(e2.__dict__)
print(Employee.__dict__)

#Class variable scope
print("Class variable: ", Employee.increment)
print("E1 instance",e1.increment, "E2 instance ", e2.increment )

#HERE CLASS VARIABLE IS UPDATE ONLY FOR THE INSTANCE
print("e1 original attribute " ,e1.__dict__)

#e1.increment = 2.0
#NOW E1 INSTACE WILL HAVE ATTRIBUTE INCREMENT
print("e1 new attribute " ,e1.__dict__)
print("Class variable: ", Employee.increment)
print("E1 instance",e1.increment, "E2 instance ", e2.increment )

#e1.raise_amt()
print("E1 Pay", e1.pay, "E2 pay", e2.pay)

#CLASS VARIABLE IS UPDATED FOR ALL INSTANCES
print("\n\n-----------------\n\n")

Employee.increment = 3.0

print("Employee raise amt()", Employee.increment)
e1.raise_amt()
e2.raise_amt()
e3 = Employee("John", "Paul",10)
print("CLASS UPDTE - Class variable: ", Employee.increment)
print("CLASS VARIABLE UPDATE E1 instance",e1.increment, "CLASS VARIABLE UPDATE E2 instance ", e2.increment )
print("E1 Pay", e1.pay, "E2 pay", e2.pay, " Pay direct from Employee Class: ")
print("\n\n third Class name ", e3.full_name(), "and Pay is: ", e3.pay, e3.raise_amt(), e3.pay)
e3 = Employee("John", "Paul",10)
print("counter", Employee.cnt)

#---output
# Employee raise amt() 3.0
# CLASS UPDTE - Class variable:  3.0
# CLASS VARIABLE UPDATE E1 instance 3.0 CLASS VARIABLE UPDATE E2 instance  3.0
# E1 Pay 300 E2 pay 600  Pay direct from Employee Class: 


#  third Class name  John Paul and Pay is:  10 None 30
# sauami@Sauami tmp % 
#counter 4 (Because cnt will increment everytime when new instance is craeted)
#--------