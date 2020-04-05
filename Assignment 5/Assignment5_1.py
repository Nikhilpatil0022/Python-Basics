x = int(input("Enter a number: "));
i = 1;
def fun():
    global i;
    if(i<=x):
        print("* ",end=" ");
        i = i+1;
        fun();


fun();