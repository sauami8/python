

age=5
print("age is ", age)
age **=2
print(age)

a=1
while a<=2:
    print(a)
    b=20
    if age==b:
        print("A is equal to b")
    else:
        print("A is not Equal to B")    
    a+=1
    b+=1


a=10
b=20

if not a!=b:
    print("Not condition")
else:
    print("else part")

def AgeCheck(age):
    if age>=18:
        return "Not Minor"
    else:
        return "Minor"

val = AgeCheck(26)
print(val)

val =AgeCheck(10)
print(val)


