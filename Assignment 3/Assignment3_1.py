x = int(input("Enter the number of elements: "))
print("Enter them one by one: ")
a=[]
for i in range(x):
    b = int(input());
    a.append(b);

tot=0
for i in range(x):
    b = a.pop();
    tot = tot + b;

print("Addition is: ",tot);