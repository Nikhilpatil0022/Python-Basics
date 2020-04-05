x=int(input("Enter the number: "))
flag=0;

for i in range(1,x):
    if(x%i==0):
        flag=1;

if(flag==1) :
    print("Prime number")
else:
    print("Not a prime number")