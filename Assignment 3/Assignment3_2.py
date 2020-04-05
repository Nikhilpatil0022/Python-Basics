x = int(input("Enter the number of elements: "))
print("Enter them one by one: ")
a=[]
for i in range(x):
    b = int(input());
    a.append(b);

high = a.pop()

for i in range(x-1):
    b = a.pop();
    if b >= high:
        high = b;

print("highest number is: ", high);