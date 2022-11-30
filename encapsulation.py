
"""encapsulation is to restrict access to the class variable restrict from direct access use __ before """


class person:
    cv = "Hello Class"
    def __init__(self, fname, lname,pay) -> None:
        self.__fname = fname
        self.__lname = lname
        self.pay = pay

    def full_name(self):
        print(f"{self.__fname}, {self.__lname}")


person_instance = person("jhon", "dow",800)

#no impact after implementing the encapsulation
person_instance.fname='Tom' #to retrict direct accesst to class variable use the encapsulation(make class variable private)
person_instance.__lname="Miller" #here it won't allow to change the value as class variables become private

person.cv="bye Class"

person_instance.full_name()

print(person.cv)

