'''n = int(input("Enter a value :"))
i = 1
while i<=n:
    if i%2==0:
        print(i)
    i= i+1'''

'''n = int (input("Enter a number : "))
for i in range (1,11):
    print(n,"x" ,i,"=",i*n)'''


n =int (input("Enter a number :"))
r=0
while n>0:
    digit = n% 10 
    r = r*10 + digit
    n = n//10
print("Reverse number :",r)