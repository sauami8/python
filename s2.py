import s1

x = print ("This is from Main S2 file and __name__ is ", __name__)
s1.x = print("This is from S1 and __name__ is {}".format(__name__))

s1.hello()



def hello():
    print("Hello S2 from {} ".format(__name__))

hello()

