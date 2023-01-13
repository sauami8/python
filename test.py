from cmd import PROMPT


a = int(input("input 1st number:"))
b = int(input("input 2nd number:"))

x = lambda a : a + 10
print(x(5))

x = lambda a,b: a + b
print(x(5,5))

#a = input('Enter value 1: ')
#b = input("Enter 2nd value: ")
c = int(input("Input: 1 for Add, 2 for Subtract, 3 for Multiply, 4 for Division: "))

if c==1 :
    o=lambda a,b: a+b
    #print(o)
elif c==2 :
    o = lambda a,b: a-b
elif c==3 :
    o = lambda a,b: a*b
elif c==4 :
    o = lambda a,b: a-b
else:
    o = "Enter correct value"
    
print(a)
print(b)
print(c)
print("Output" , o(a,b))
