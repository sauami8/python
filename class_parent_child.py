

from tarfile import PAX_NAME_FIELDS


class emp:
    def __init__(self, fname, lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.'+lname + '@company.com'
s
    def pname(self):
        print(f"Emp name {self.fname}, {self.lname} ")

class n(emp):
    def __init__(self, fname, lname, pay, v):
        super().__init__(fname,lname,pay)
        self.v = v

    def print_name(self):
        print(f"emp name {self.fname}, {self.lname} and value is {self.v}", )

e = emp("Jack", "Ryan", 100)

e1 = n('Jack','Son',500, 5)

e1.print_name()
e1.pname()
e.pname()
x = [e.fname, e.lname]

print(x)