
class employee:
    
    pay_raise = 1

    def __init__(self, fname, lname, pay) -> None:
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@email.com'
    
    def full_name(self):
        print(f'Employee full name is --> {self.fname} {self.lname} <-- and emial is --> {self.email} <-- pay is {self.pay}')


    def new_pay(self):
        np = int(self.pay * self.pay_raise)
        return f'{self.fname}, {self.lname}  old pay is {self.pay}   new pay is {np}'

    @classmethod
    def from_string(cls, emp_str):
        fname1, lname1, pay1 = emp_str.split('-')
        return cls(fname1, lname1, pay1)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday()==6:
            return False
        return True

    # this is add method to add two employee instance pay together, if you don't add thid method to calss than it will 
    # error out as it doesn't know how to add two employee
    def __add__(self, other):
        return self.pay + other.pay



# Static method
import datetime
mydate = datetime.date(2022,12,9)
print(employee.is_workday(mydate))
# -------------
  
#----classmethod use decorator and create function initial name 'from_' instead of self use 'cls' for class 
# and variable to pass to the class to instanciate the class instance
#  
emp_str = 'Joe-Wheeler-1000'
f,l,p = emp_str.split('-')
# print(f,l,p)
# this create instance of employee class with values retrieve from emp_str variable 
alt_emp_inst = employee.from_string(emp_str)
print('alternate emp instance -->')
alt_emp_inst.full_name()
print(alt_emp_inst.pay_raise)

print(alt_emp_inst.__dict__)
#-----

emp1 = employee('John', 'Dow', 5000)
emp1.pay_raise = 1.1

emp2 = employee('John', 'Dow', 5000)
twopay = emp1+emp2
print("two employee together pay --> ", twopay)

print('Emp 1 pay rise', emp1.new_pay())

print('Emp 2 pay rise', emp2.new_pay())

print(emp1.new_pay())
# print('this is instance' , emp1.__dict__)
print('this is Class' , employee.__dict__)

