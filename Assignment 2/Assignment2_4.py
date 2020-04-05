x=int(input("Enter the number: "))
add=0;
for i in range(1,x):
    if(x%i==0):
        add=add+i;

print("Addition of factors is: ",add);