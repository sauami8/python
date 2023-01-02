# import logging
# log = logging.getLogger("PR_MAIN")
# log.error("Here is the error1")

def add(x, y):
    """Add function"""
    return x+y

def subtract(x, y):
    """Subtract function"""
    return x - y

def multiply(x, y):
    """multiply function"""
    return x*y

def divide(x, y):
    """Divide function"""
    return x/y

n1 = 20
n2 = 10

import logging
import time as t

logging.basicConfig(filename='pkg/mylog.log', level=logging.DEBUG, 
    format='%(asctime)s:%(levelname)s:%(funcName)s: %(filename)s:%(message)s')

# default logging level is Warning, here level is set at debug level to run the below statment or you can 
# run with warning without setting it to DEBUG
# https://docs.python.org/3/library/logging.html

add_result = add(n1,n2)
logging.debug('Add: {}+{} = {}'.format(n1,n2,add_result))

sub_result = subtract(n1,n2)
logging.debug('Subtract {}-{} = {}'.format(n1,n2,sub_result))

mul_result = multiply(n1,n2)
logging.debug('Multiplication of {}x{} = {}'.format(n1,n2,mul_result))

div_result = divide(n1,n2)
logging.debug('Division {}/{} = {}'.format(n1,n2,div_result))







# add_result = add(n1,n2)
# print('Add: {}+{} = {}'.format(n1,n2,add_result))

# sub_result = subtract(n1,n2)
# print('Subtract {}-{} = {}'.format(n1,n2,sub_result))

# mul_result = multiply(n1,n2)
# print('Multiplication of {}x{} = {}'.format(n1,n2,mul_result))

# div_result = divide(n1,n2)
# print('Division {}/{} = {}'.format(n1,n2,div_result))

# Class logging
# import logging

# logging.basicConfig(filename='pkg/class_example.log', level=logging.INFO, 
# format='%(asctime)s:%(levelname)s:%(funcName)s:%(message)s')

# class country:
#     def __init__(self, city, lang):
#         self.city = city
#         self.lang = lang
    
#     def getcity(self):
#         # print(f"{self.city} is city")
#         logging.info('{} is city'.format(self.city))
    
#     def getlang(self):
#         # print(f"{self.lang} is primary language")
#         logging.info('{} is primary language'.format(self.lang))

# queen = country('London', 'English')
# takila = country('Maxico', 'Spanish')


# for countrydetail in (queen, takila):
#     countrydetail.getcity()
#     countrydetail.getlang()

# class Cars:
#     def __init__(self, speed, color) -> None:
#         self.__speed = speed # set speed as private
#         self.color = color

#     class_color = "Yello"
    
#     def get_speed(self):
#         print(f'Car Speed is --> {self.__speed}')
    
#     def get_color(self):
#         print(f'Car color is --> {self.color}')
    
#     def set_speed(self, v):
#         self.__speed = v
    
#     def set_color(self, c):
#         self.color = c
    

# vw = Cars(120,'White')

# vw.get_speed()
# vw.get_color()
# vw.set_speed(200)
# vw.get_speed()
# vw.__speed = 300 # private variable speed can not be set manually
# vw.get_speed()

# ford = Cars(90,'Red')
# print(ford.color)
# ford.set_color('Blue')
# ford.get_color()
# print(ford.color)
# Cars.class_color = 'Orange'
# print(f'Class variable color  --> {Cars.class_color}')
# ford.get_color()

