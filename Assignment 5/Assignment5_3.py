x = int(input("Enter a number: "));

def fun(i):
    global x;
    if(i<=x):
        fun(i+1);
        print(i, end=" ");


fun(1);