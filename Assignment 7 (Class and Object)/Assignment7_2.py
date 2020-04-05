class BankAccount :
    ROI = 10.5;

    def __init__(self,Name,Ammount):
        self.Name = Name;
        self.Ammount = Ammount;

    def Display(self):
        print("Name:- " + self.Name +" Account Balance ", self.Ammount);

    def Deposit(self,amt):
        self.Ammount += amt;

    def Withdraw(self,amt):
        self.Ammount -= amt;

    def CalcInterest(self):
        interest = self.Ammount*BankAccount.ROI/100;
        print("Interest on your ammount " , self.Ammount ," is ",interest);

def main():
    obj1 = BankAccount("Robert Love",10000);
    obj1.Display();
    obj1.Deposit(5000)
    obj1.Display();
    obj1.Withdraw(2000);
    obj1.Display();
    obj1.CalcInterest();


    obj2 = BankAccount("Dennis Ritchie",20000);
    obj2.Display();
    obj2.Deposit(5000)
    obj2.Display();
    obj2.Withdraw(2000);
    obj2.Display();
    obj2.CalcInterest();


if __name__=="__main__":
    main();