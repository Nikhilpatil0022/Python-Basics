n=input("Enter a number:");
tot=0;
y=list();
for i in range(len(n)):
    y.append(int(n[i]));

for i in range(len(y)):
    tot=tot+y[i];
print("sum of digits is: ",tot);