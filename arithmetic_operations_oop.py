class Arithmetic_op:
    a = None
    b = None

    def getData(self):
        self.a = int(input("Enter a number"))
        self.b = int(input("Enter b number"))

    def show_results(self):
        print("addition = " + str(self.a + self.b))
        print("subtraction = " + str(self.a - self.b))
        print("division = " + str(self.a / self.b))
        print("multiplication = " + str(self.a * self.b))

    
arith = Arithmetic_op()

arith.getData()
arith.show_results()