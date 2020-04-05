x = int(input("Enter the number of elements: "))
print("Enter them one by one: ")
a=[]
for i in range(x):
    b = int(input());
    a.append(b);

print("Enter number to be searched")
b=int(input())
count = 0
for i in range(x):
    if b==a[i]:
        count+=1;

print("Frequency of the number is: ",count)