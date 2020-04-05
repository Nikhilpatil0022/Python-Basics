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


def ChkNum(b):
    if(b>=70 and b<=90):
        return True;
    else:
        return False;


def modify(b):
    return b+10;


def sum(no1,no2):
    return no1 + no2;


def main():
    RawData = accept();
    print("Entered data is: ")
    print(RawData);

    filteredData = list(filter(ChkNum,RawData));
    print("Filtered Data(Between 70 and 90) is: ")
    print(filteredData);

    modifiedData = list(map(modify,filteredData));
    print("modified data(adding 10) is: ")
    print(modifiedData);

    result = reduce(sum,modifiedData);
    print("Reduced data(Sum) is: ",result);


if __name__ == "__main__":
    main();