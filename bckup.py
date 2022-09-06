
print("KM to Mile converter")

num1 = 10 #float(input("Enter KM: "))
mile = num1/1.609
print(round(mile,2), "total mile in", round(num1,2)," Km")


radious = float(input("Enter the Radious of a circle"))

import math as m

area = m.pi * (radious**2)
print("Area is ", round(area,2))


f = 'saurabh' #input("enter your first name")
m = 'raj' #input("enter your mid name")
s = 'mish' #input("enter your surname")

print()
print()

print("Your initials are ",'"'+f[0], m[0],s[0]+'"')


radious =10# float(input("Enter the Radious of a circle"))

import math as m

area = m.pi * (radious**2)
print("Area is ", round(area,2))


l = ["marry", "Jerry", "Larry"]
print(l)

additem = input("Add item in list")
l.append(additem)
print()
print()


d = {
    "name": "Tom",
    "city": "Coppell",
    "country": "US"
}

x = input("Enter the informaton you want to see: ").lower()

result = d.get(x, "Info is not available")
print(x, "Value is " , result)

k = input("Enter key you want to add to Dict: ").lower()

v = input("Enter value you want to key: ").lower()

d.update({k:v})

print(d)

print()

i1 = float(input("enter first number: "))

i2 = float(input("Enter 2nd Number: "))

if (i1 == i2):
    print(f"num2 is equal to num2")
elif (i1 < i2):
    print("num1 is less than num2")
else:
    print("num1 is greater than num2")



#Number game
import random

num = random.randint(1,10)

print("Welcome to the number Guessing Game, You have 5 Chances to Win")

d = input("You want to Play ?. Enter your Choice Y/N ").lower()

if (d=='y' or d=='yes'):    
    guess = int(input("enter your guess num: "))

    i=0
    while True:
        i+=1
        #print("Random number is: ",num)
        if i==5:
            print("You Failed to Guess the Number")
            print("Better Luck Next time and Thanks for Playing.... :)")
            print("Number you were Guessing Was--> ",num)
            break    
        if (num==guess):
            print("Congratulations You Guessed It :), number was ", num)
            break
        else:
            guess = int(input("try again: "))

else:
    print("Come back Again... thanks")
    
#delete key from dict
d.pop("add")
#clear the dict
d.clear()

# dict for loop key and value
d = {'name': 'value', 'age': 20, 'gender': 'm'}
for x in d:
    print(x, "value is ",d[x])

#list loop for element and each character
l2 = ['Ram', 'Tom', 'Jay', 'Sia', 'Tim', 'Saurabh', 'Karen', 'Laura']
for x in l2:
    print(x)
    for y in x:
        print(y)

#continue expression allow to jump to the loop without further evaluating the remaining code condition
for lv in l:
    if lv=="":
        continue
        #below statment will not be execute as cursor will jump to begning of the loop
        print("test for blank")
    else:
        print(lv)

#2nd example for contineue
chk = False

while chk == False:
    n1 = float(input("Enter the First Number between 1 to 10: "))
    if (n1 <1 or n1>10):
        print("Enter the number between 1 to 10")
        continue
    else:
        print('b')
        chk =True

print("your number is: ", n1)

#----Random Selection 
l = ["Tom","Jack", "Defney","Jenny","Laura","Jenny","Peter"]

import random

for r in range(0,2):
    n = input("Enter name for selection: ")
    l.append(n)
    print(l)

p = random.randint(0,8)
print("1st Selected name is: ",p, l[p])
p = random.randint(0,8)
print("2nd Selected name is: ",p, l[p])
p = random.randint(0,8)
print("3rd Selected name is: ",p, l[p])

for xx in range(1,10):
    p1 = random.randint(0,8)
    print(xx ," Selection is: ", l[p1])

#------------
#----Game
import random

num = random.randint(1,10)

print("Welcome to the number Guessing Game, You have 5 Chances to Win")

d = input("You want to Play ?. Enter your Choice Y/N ").lower()

if (d=='y' or d=='yes'):    
    guess = int(input("enter your guess num: "))

    i=0
    while True:
        i+=1
        #print("Random number is: ",num)
        if i==5:
            print("You Failed to Guess the Number")
            print("Better Luck Next time and Thanks for Playing.... :)")
            print("Number you were Guessing Was--> ",num)
            break    
        if (num==guess):
            print("Congratulations You Guessed It :), number was ", num)
            break
        else:
            guess = int(input("try again: "))

else:
    print("Come back Again... thanks")
    
#-----------------

#try and except error

chk = False

while chk == False:
    n1 = float(input("Enter the First Number between 1 to 10: "))
    if (n1 <1 or n1>10):
        print("Enter the number between 1 to 10")
        continue
    else:
        print('b')
        chk =True

print("your number is: ", n1)


while chk==True:
    n2=input("Enter your 1st number: ")
    try:
        n2 = float(n2)
        chk=False
        print("Valid Number")
    except:
        print(f"invalid number {n2}")


a=10
for aa in range(0,5):
    x = input("Enter number: ")
    try:
        x = float(x)
        if x==a:
            print("break")
            break
        else:
            print("else part")
    except:
        print("Invalid Input")

        
    a=True
import random

while a==True:
    x = float(input("Enter number"))
    r = random.randint(0,10)
    if (x==r):
        print("you're guess is correct")
        break
        #a=False
    #both break and False work to break the while loop
    else:
        i = input("you want to continue to play")
        if i=='y':
            print("hello")
        else:
            print("thanks for play9ng")
            break
            
    
#file operation txt file read and write
f = open("file.txt","r")
print(f.read())

#open the file and then write to the file, write operation overwrite the content of the file

f=open("file1.txt","w")
f.write("Overwriting the file with new content")

f = open("file1.txt","r")
print(f.read())

#append operation to append data to file point to remember - include new line operator

f = open("file1.txt","a")
f.write("\nHello world, appending the data123")

f = open("file1.txt","r")
print(f.read())


#Unary operator - negate the number and return the opposite sign number by adding for subtracting as per sign
# if ~-9 ==OutPut> 8     if ~9 ==> -10
a=10
b=-10

if b==~9:
    print("b-10 compare with b=~9")
else:
    print("nothing")


 #Creating function with variable number of Argument

def say_hello(varcount=0, *vararg):
    print(f"You have passed {varcount} number of argument to function")
    for v in vararg:
        print("Argument values are: ",v)



              
   #Excel import and data frame

   # require pandas and rdxl module to work with excel file

import pandas as pd

# variable to hold the excel file info

file = pd.ExcelFile("sample_superstore.xls")

#get excel sheet information

print(f.sheet_names)

# Variable will hold the excel file sheets info
# to load the sheet data into pd dataframe variable need to parse for sheet in eg people sheet is used

df = file.parse("People")

print(df)

# to access the specifix record from index
df.loc[1]

#to acccess the column values for dataframe
df["Region"]

#query multicolumn from df by index
df.loc[1,"Person":"Region"]


# check the records in dataframe based on column specific value

sheet.loc[sheet["Country"]=="United States"]

#check DF any column values
heet.Category   or  sheet.Country

#check specific row and column values
sheet.loc[1,"Quantity":"Profit"]


#Set Custome index on DF to enable direct search on the column for specific values
#here index set on "Category" field to search records for specific values
sheet.set_index("Category", inplace=True)
sheet.loc["Furniture"]

#Reset the index

