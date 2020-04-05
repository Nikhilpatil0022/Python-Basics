import MarvellousNum as M;
def listPrime(a):
    for i in range(x):
        flag = 0;
        if(a[i]> 1):
            for j in range(2, a[i]):
                if(int(a[i]) % j == 0):
                    flag = 1;
        if flag == 0:
            L.append(a[i]);
    print("List of prime numbers is: ");
    print(L);
    sum = 0
    for i in range(len(L)):
        sum += L[i];
    print("Their addition is: ",sum)

x = int(input("Enter the number of elements: "))
print("Enter them one by one: ")
a=[]
L=[]
for i in range(x):
    b = int(input());
    a.append(b);
print(a);
listPrime(a);

for i in range(x):
    M.chkPrime(a[i]);