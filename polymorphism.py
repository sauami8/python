"""Ability to take or have various forms
for example Mobile phone can used as Camera or MP3 Player or Calling Phone
"""


def add_num(a,b,c=0):
    return (a+b+c)

print(add_num(4,8), end='/')
print(add_num(4,8,4))

class ind:
    def city(self):
        print("Delhi is City of India")
    
    def language(self):
        print("Many languages are spoken in India")


class us:
    def city(self):
        print("Coppel is the city of US")
    
    def language(self):
        print("English is primary language in USA")


india = ind()
usa = us()

# india.city()
# usa.language()

def print_info(obj):
    return obj

for countries in (india,usa):
    print_info(countries.city())
    print_info(countries.language())
    countries.city()

print("\n\n\n ----")

for ob in (india,usa):
    ob.city()
    ob.language()

print_info(india.city())

# calc

