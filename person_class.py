

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def print_name(self):
        print(f"First name {self.fname} and Last name is {self.lname}")

person = Person('Jhon', 'Dow')
person.print_name()


class Sub(Person):
    def __init__(self, fname,lname,city):
        super().__init__(fname, lname)
        self.city = city
    
    def print_info(self):
        txt = f"Person {self.fname}, {self.lname} lives in {self.city}"
        return txt

subperson = Sub('Rosy','Day','SFO')

subperson.print_name()
info = subperson.print_info()
print(info)

def method_take_class(cls):
    val = cls.print_info()
    return val

m = method_take_class(subperson)
print('This is method called the class instance ',m)

print("\n\t\t------------")

class UK:
    city = 'London'
    def capital(self):
        print("Capital of UK is London")
    
    def lang(self):
        print("English is UK official language")

class spain:
    def capital(self):
        print('Madrid is Capital of Spain')
    def lang(self):
        print("Spanish is primary language")

# instanciate the class

queen = UK()
zara = spain()

for info in (queen, zara):
    info.capital()
    info.lang()


def instance_info(ins):
    ins.capital()
    ins.lang()
    print('Accessing the instance Attribute', ins.city)

instance_info(queen)