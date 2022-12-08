# class Employee:
#     pass

# emp = Employee()
# emp1 = Employee()

# emp.fname = 'Jhon'  # type: ignore
# emp.lname = 'Dow'
# emp.email = 'jhon.dow@email.com'

# emp1.fname='Tom'
# emp1.lname = 'Cruse'
# emp1.email = emp1.fname + '.'+ emp1.lname + '@email.com'

# print(emp.email, emp)
# print(emp1.email, emp1)

# Above is manual and tedious way to create employee records to avoid repetative task every time 
# we can create class and re-use them by creating instance of the class

class emp_cls:
    city='work'
    def __init__(self, fname, lname, pay) -> None:
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + 'lname' + '@email.com'
    
    def full_name(self):
        fullname = self.fname + ' ' + self.lname
        return fullname

    def hello():
        print('Class hello function without self')

emp_ins = emp_cls('Jhon', 'Dow', 5000)

print(emp_ins.full_name())

print(emp_cls.full_name(emp_ins)) # here function is called with class and pass the instance for self this is what exactly happned in background

print(emp_cls.hello) # <function emp_cls.hello at 0x102ce8820>

# Class variable vs instance variable
# Important: if instance variable is not set explicitly, Class Variable update with take effect to instance variable
# emp_ins.city='Ind'
emp_cls.city='US'
print(emp_cls.city, emp_ins.city)




