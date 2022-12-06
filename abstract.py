from abc import abstractclassmethod, ABC

class Abs_class:
    @abstractclassmethod
    def area(l,w):
        pass

    @abstractclassmethod
    def perimeter(l,w):
        pass

class Abs_imp(Abs_class):
    def __init__(self, l=1,w=1) -> None:
        # super().__init__()
        self.l = l
        self.w = w
    
    def area(self, ll, ww):
        self.l = ll
        self.w = ww
        a = self.l * self.w
        return a
    
    def perimeter(self, ll, ww):
        self.l = ll
        self.w = ww
        p = (2*self.l) + (2*self.w)
        return p
    

calc = Abs_imp()
    
print(f'Are of Length {calc.l} and width {calc.w} is {calc.area(3,2)}')
print(f'Perimeter of length {calc.l} and width {calc.w} is {calc.perimeter(3,2)}')


print(f'Area of Length {calc.l} and width {calc.w} is {calc.area(5,5)}')
# find the problem why value of length and width is not correctly showing, however calclation is correct as per input
# :) in third display value remain same until next function call to change the value, here area function is called after display value

input_l = int(input('Enter the length: '))
input_w = int(input('Enter the Width: '))

print(f'Area of Length {input_l} and width {input_w} is {calc.area(input_l,input_w)}')