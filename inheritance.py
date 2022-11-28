from numpy import isin


class person:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname
        self.full_name = fname + ' ' +lname
    
    def print_name(self):
        return self.full_name

class new_person(person):
    def __init__(self, fname, lname) -> None:
        super().__init__(fname, lname)
        self.full_name = lname + ', ' + fname #this overwrite parent class full_name variable
    
    def print_name(self):
        return self.fname + '-'+self.lname


class new_person2(new_person):
    def __init__(self, fname, lname,pay) -> None:
        super().__init__(fname, lname)
        self.pay = pay
        self.email = fname+'.'+lname+'@email.com'

    def print_name(self):
        return self.fname+self.email

    """Another new class inherit from parent class to include the pay detail of the employee
    also you can observe that print_name method not even defined in parent class new_person
    because this class inherit the print_name function from its parent 
    if child class have method name same as parent class in this class childern Class take pracidence
    """



emp_name = person("Jhon", "Miller")
new_name = new_person("Jhon", "Miller")
new_name2 = new_person2("Jhon", "Dow",800)

print(f"Person class emp full name --> {(emp_name.print_name())}")

print(f"Inherit New person Class emp name in reverse {new_name.print_name()}")

print("new name2 emp name {} and pay is {}".format(new_name2.print_name(),new_name2.pay))



# if isinstance(new_name, person):
#     print("emp_name is instance of Person Class {}".format(new_name.print_name))
# else:
#     print("not a instance")