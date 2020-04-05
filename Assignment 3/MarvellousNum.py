def chkPrime(x):
    flag = 0;
    for i in range(2,x):
        if(x % i == 0):
            flag = 1;
            break;
    if flag == 0:
        print(x, " is a Prime no")
    else:
        print(x, " is NOT a Prime no")