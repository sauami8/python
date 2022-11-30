

class emp:
    v = "Hello Class"
    def __init__(self, fname, lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.'+lname + '@company.com'

    def pname(self):
        print(f"Emp name {self.fname}, {self.lname} and pay is {self.pay} ")

    def __add__(self, other):
        return self.pay + other.pay

    def add_val(self, msg):
        print(f"Hello {self.email}, and {msg}")
    
    def gv(self,v):
        print("printing class variable ", v)

class n(emp):
    def __init__(self, fname, lname, pay, v):
        super().__init__(fname,lname,pay)
        if self.v is None:
            self.v = []
        else:
            self.v = v

    def print_name(self):
        for x in self.v:
            print("emp name ", )

e = emp("Jack", "Ryan", 200)

e1 = emp("Peter", "Singh", 300)

greet = e1.add_val("How are you doing")
print(greet)

print("adding two instance pay ",e+e1)


print(e.pay)

e.v = 'some value'
emp.v = 'bye class'
e.pname()
print(e1.v, e.v)
emp.v = 'bye class'

print(e.v, emp.v, e1.v)


e.gv(e.v)

"""
#class to add employee to list 
class emp:
    l = ['jay']
    def __init__(self, ename):
        self.ename = ename

    def add_emp(self,name):
        if name in self.l:
            print("emp in list")
        else:
            print("emp added in list")
            self.l.append(name)

            
e = emp("tom")
e.l
['jay']
e.add_emp("raj")
emp added in list
e.l
['jay', 'raj']
e.add_emp("rosy")
emp added in list
e.;
SyntaxError: invalid syntax
e.l
['jay', 'raj', 'rosy']
e.add_emp('raj')
emp in list
e.l
['jay', 'raj', 'rosy']
#-----------------------

"""