from functools import reduce;
def accept():
    print("Total Numbers? ");
    x = int(input());
    a = [];
    print("Enter those numbers ");
    for i in range(x):
        c = int(input());
        a.append(c);
    return a;


def ChkPrime(b):
    flag = 0;
    for i in range(2,b):
        if(b%i ==0):
            flag = 1;
            break;
        else:
            flag =0 ;
    if(flag == 0):
        return True;
    else:
        return False;


def modify(b):
    return b*2;


def maxi(no1,no2):
    if(no1>=no2):
        return no1;
    else:
        return no2;


def main():
    RawData = accept();
    print("Entered data is: ")
    print(RawData);

    filteredData = list(filter(ChkPrime,RawData));
    print("Filtered Data (Prime) is: ")
    print(filteredData);

    modifiedData = list(map(modify,filteredData));
    print("Modified data(*2) is: ")
    print(modifiedData);

    result = reduce(maxi,modifiedData);
    print("Reduced data(Max) is: ",result);


if __name__ == "__main__":
    main();