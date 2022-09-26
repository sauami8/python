

from tarfile import PAX_NAME_FIELDS


class emp:
    def __init__(self, fname, lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.'+lname + '@company.com'

    def pname(self):
        print(f"Emp name {self.fname}, {self.lname} ")

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

e = emp("Jack", "Ryan", 100)

x = [e.fname, e.lname]

print(x)