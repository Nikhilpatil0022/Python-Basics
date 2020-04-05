x = int(input("Enter the number of elements: "))
print("Enter them one by one: ")
a=[]
for i in range(x):
    b = int(input());
    a.append(b);

low = a.pop()

for i in range(x-1):
    b = a.pop();
    if low >= b:
        low = b;

print("lowest number is: ", low);