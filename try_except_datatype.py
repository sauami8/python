
import try1 as t1
print(t1.a)

x = input('Enter Number: ')

try:
    val = int(x)
except ValueError as e:
    print('Wrong Input type', e)
else:
    print('value of x is ',val)
finally:
    print('final statment closure')


# # a=True
# while True:
#     try:
#         a = float(input('Enter the object value ==> '))
#         print('type of a is ',type(a))
#         type(a) == int
#         if type(a)==int:
#             print('Input type is Integer')
#         elif type(a)==bool:
#             print('Input type is  bool')
#         elif type(a)==str:
#             print('Input type is  string')
#         elif type(a)==list:
#             print('Input type is its list')
#         elif type(a) == float:
#             print('Input Number is Float')
#         else:
#             print('Type is not defined, lets research')
#         break
#     except:
#         print('something else Try again')
        

# for i in range(1,10):
#     if i==3:
#         continue
#     else:
#         print('numner is ',i)


# while True:
#     try:
#         a = input("Enter number: ")
#         a = int(a)
#         print("number squar is", a**a)
        
#     except:
#         print('not a number')
#         break