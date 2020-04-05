class Arithmetic:
    def __init__(self):
        self.value1 = 0;
        self.value2 = 0;
        self.Add = 0;


    def Accept(self):
        print("Enter 2 values: ");
        self.value1 = float(input());
        self.value2 = float(input());


    def Addition(self):
        self.Add = float(self.value1+self.value2);
        print("Addition is: ",self.Add);


    def Substract(self):
        self.Sub = float(self.value1-self.value2);
        print("Substraction is: ", self.Sub);

    def Division(self):
        self.Div = float(self.value1 / self.value2);
        print("Division is: ", self.Div);


    def Multiply(self):
        self.Mult = float(self.value1 * self.value2);
        print("Multiplication is: ", self.Mult);


def main():
    obj1 = Arithmetic();

    obj1.Accept();
    obj1.Addition();
    obj1.Substract();
    obj1.Division();
    obj1.Multiply();

    obj2 = Arithmetic();

    obj2.Accept();
    obj2.Addition();
    obj2.Substract();
    obj2.Division();
    obj2.Multiply();


if __name__ == '__main__':
    main();