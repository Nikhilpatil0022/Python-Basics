x=int(input("Enter a number for factorial: "))
fact=1;
if(x==0):
    print("factorial of 0 is 1");
else:
    for i in range (1,x+1):
        fact=fact*i;

print("Factorial of ",x ,"is ",fact);