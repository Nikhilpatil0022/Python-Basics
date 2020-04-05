x = int(input("Enter a number: "));

def fun(i):
    if(i<=x):
        print(i,end=" ");
        fun(i+1);


fun(1);