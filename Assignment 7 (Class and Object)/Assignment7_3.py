class Number:
    def __init__(self,x):
        self.x = x;

    def ChkPrime(self):
        flag = 0;
        for i in range(2,self.x):
            if (self.x%i == 0):
                flag = 1;
                pass;
        if(flag == 1):
            print("Not a Prime Number");
            return False;
        print("Prime Number");
        return True;

    def Factors(self):
        L = [];
        for i in range(1, self.x):
            if (self.x % i == 0):
                L.append(i);
        print("Factors of ",self.x ," are ",L);
        return L;


    def ChkPerfect(self):
        sum = self.SumFactors();
        if (sum == self.x):
            print("Perfect Number");
            return True;

        print("Not a Perfect Number");
        return False;


    def SumFactors(self):
        L = [];
        L = self.Factors();
        sum = 0;
        for i in range(len(L)):
            sum += L[i];
        print("Sum of factors is ",sum);
        return sum;

def main():
   obj1 = Number(7);
   obj1.ChkPerfect();
   obj1.ChkPrime();
   print();
   print();
   print();
   obj2 = Number(6);
   obj2.ChkPerfect();
   obj2.ChkPrime();


if __name__=="__main__":
    main();