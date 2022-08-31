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
    
