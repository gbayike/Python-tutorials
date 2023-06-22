class Marks:
    a = None
    b = None
    c = None
    sum = None

    def set_marks(self):
        self.a = int(input("Ener 1st mark "))
        self.b = int(input("Ener 2nd mark "))
        self.c = int(input("Ener 3rd mark "))

    def sum_func(self):
        self.sum = self.a+self.b+self.c
        print(self.sum)

    def avg(self):
        average = self.sum / 3
        print(average)


obj = Marks()
obj.set_marks()
obj.sum_func()
obj.avg()