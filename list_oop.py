class List:
    lst = []

    def get_data(self):
        for i in range(5):
            self.lst.append(int(input("Enter a number")))

    def max(self):
        print(self.lst)
        print(max(self.lst))


lst = List()

lst.get_data()
lst.max()