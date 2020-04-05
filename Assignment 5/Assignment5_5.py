x = int(input("Enter a number: "));
fact = 1

def fun(x):
    global fact;
    if(x > 0):
        fact=fact * x;
        fun(x-1);


fun(x);
print("Factorial is: ",fact);