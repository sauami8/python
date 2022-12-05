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