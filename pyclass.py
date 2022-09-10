# empty class
class emp:
    pass

#Class instace Class is simple blue print in this case e1 and e2 and both have different location in memory
e1 = emp()
e2 = emp()

print(e1)
print(e2)
# <__main__.emp object at 0x104a67f40>
# <__main__.emp object at 0x104a67f10>

class employee:

    #__init__ function call when instance is created and instance is passed in place of self without mentioning

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'
    
    def full_name(self):
        return "{} {}".format(self.fname,self.lname)

#create instance of the class with the value in the order defined in class init 

e1 = employee('saurabh', 'raj',1000000)
e2= employee("Hari","om",2000000)

print(e1.fname, e1.email)
print(e2.lname,e2.fname, e2.email)
print(e1)#this will tell that its object at memory location like <__main__.employee object at 0x1051fbeb0>

#Created the function to give full name now we can use the previously created instace of the class to get respected name
#let use both one after anohter
print("First instanace full name" , e1.full_name())
print("Full name from 2nd Instance", e2.full_name())

#we can directly use the class and method but in this case need to pass instance because full_name method take one parameter self which is instance

print(employee.full_name(e2))
#But in case of instance which have all parameters while creating instance and instance which have necessary parameter
# is passed to fullname func as self automatically 
print(e2.full_name())