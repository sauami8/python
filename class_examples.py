class country:
    def __init__(self, city, lang):
        self.city = city
        self.lang = lang
    
    def getcity(self):
        print(f"{self.city} is city")
    
    def getlang(self):
        print(f"{self.lang} is primary language")

queen = country('London', 'English')
takila = country('Maxico', 'Spanish')


for countrydetail in (queen, takila):
    countrydetail.getcity()
    countrydetail.getlang()

class Cars:
    def __init__(self, speed, color) -> None:
        self.__speed = speed # set speed as private
        self.color = color

    class_color = "Yello"
    
    def get_speed(self):
        print(f'Car Speed is --> {self.__speed}')
    
    def get_color(self):
        print(f'Car color is --> {self.color}')
    
    def set_speed(self, v):
        self.__speed = v
    
    def set_color(self, c):
        self.color = c
    

vw = Cars(120,'White')

vw.get_speed()
vw.get_color()
vw.set_speed(200)
vw.get_speed()
vw.__speed = 300 # private variable speed can not be set manually
vw.get_speed()

ford = Cars(90,'Red')
print(ford.color)
ford.set_color('Blue')
ford.get_color()
print(ford.color)
Cars.class_color = 'Orange'
print(f'Class variable color  --> {Cars.class_color}')
ford.get_color()

