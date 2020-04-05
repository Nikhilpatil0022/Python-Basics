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


def ChkEven(b):
    if(b%2 == 0):
        return True;
    else:
        return False;


def modify(b):
    return b*b;


def sum(no1,no2):
    return no1 + no2;


def main():
    RawData = accept();
    print("Entered data is: ")
    print(RawData);

    filteredData = list(filter(ChkEven,RawData));
    print("Filtered Data (Even) is: ")
    print(filteredData);

    modifiedData = list(map(modify,filteredData));
    print("Modified data(Square) is: ")
    print(modifiedData);

    result = reduce(sum,modifiedData);
    print("Reduced data(Sum) is: ",result);


if __name__ == "__main__":
    main();