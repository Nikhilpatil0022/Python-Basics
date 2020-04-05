x = int(input("Enter a number: "));
sum = 0

def fun(x):
    global sum;
    if(x > 0):
        y = int(x % 10);
        sum=sum + y;
        fun(int(x/10));


fun(x);
print("Sum of digits is: ",sum);