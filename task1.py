'''num1 = int (input("Enter the value of A : "))
num2 = int (input("Enter the value of B : "))
num3 = int (input("Enter the value of C : "))
if(num1>num2)and(num1>num3):
    print(num1,"is largest")
else:
    if(num2>num1)and(num2>num3):
        print(num2,"is Largest")
    else:
        print(num3,"is Largest")'''
'''n = int (input("Enter your Age :"))
if(n>=18):
    print("Your are Eligible to vote")
else:
    print ("Your not Eligible to Vote")'''
n = int (input("Enter your Mark : "))
if (n>=90 and n<=100):
    print("your mark",n,"get A grade")
elif(n>=75 and n<=89):
    print ("your mark",n,"get B grade")
elif(n>=60 and n<=74):
    print("your mark",n,"get C grade")
elif(n>=40 and n<=59):
    print ("your mark ",n,"get D grade")
else:
    print("you get below mark",n,"So your fail")

