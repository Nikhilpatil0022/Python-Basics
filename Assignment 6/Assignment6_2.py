class Circle:
    PI = 3.14;
    def __init__(self):
        self.R = 0;
        self.Area = 0;
        self.Circumference = 0;
    def Accept(self):
        self.R = float(input("Enter Radius of the Circle: "));


    def calcArea(self):
        self.Area = float(Circle.PI*self.R*self.R);


    def calcCircumference(self):
        self.Circumference = float(2*Circle.PI*self.R);


    def Display(self):
        print("Radius of circle is: ",self.R);
        print("Area of circle is: ", float(self.Area));
        print("Circumference of circle is: ", float(self.Circumference));



def main():
    obj1 = Circle();

    obj1.Accept();
    obj1.calcArea();
    obj1.calcCircumference();
    obj1.Display();

if __name__ == '__main__':
    main();