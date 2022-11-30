

class Emp:
    increment = 1.05
    cnt = 0

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        
        Emp.cnt +=1 

    def pay_raise(self):
        self.pay = int(self.pay * self.increment)
        #int(self.pay * Emp.increment) when set this instance setting instance increment will not take effect as its always look for class level variable value
        #int(self.pay * self.increment) this will consider the increment value set at instance level
        """
        e1 = Emp("Rose", "Water", 10)
        e2 = Emp("Jenny", "Shaw", 100)
        e1.increment = 2.0
        e2.increment = 3.0
        Emp.increment = 5.0

        for int(self.pay * self.increment) 
        Emp.increment  5.0
        E1.increment  2.0
        E2.increment  3.0
        E1 Pay  20
        E2 Pay  300
        Emp PayIncrease  5.0
        sauami@Sauami tmp % 

        for int(self.pay * Emp.increment)#no matter what you set at instance level it will calculate @Class level increment which is 5.0
        Emp.increment  5.0
        E1.increment  2.0
        E2.increment  3.0
        E1 Pay  50
        E2 Pay  500
        Emp PayIncrease  5.0
        """

    def full_name(self):
        return (self.fname+' '+self.lname)


e1 = Emp("Rose", "Water", 10)
e2 = Emp("Jenny", "Shaw", 100)

print("B4 Emp.increment ", Emp.increment)
print("E1.increment ", e1.increment)
print("E2.increment ", e2.increment)
print("\n\n\n\n")
e1.increment = 2.0
e2.increment = 3.0
Emp.increment = 5.0

print("Emp.increment ", Emp.increment)
print("E1.increment ", e1.increment)
print("E2.increment ", e2.increment)
e2.pay_raise()
e1.pay_raise()


print("E1 Pay ", e1.pay)
print("E2 Pay ", e2.pay)
print("Emp PayIncrease ", Emp.increment)