class Test:
    __a = None
    def set_a(self):
        self.__a = input("Enter a word ") 

    def get_a(self):
        print(self.__a)


obj = Test()
obj.set_a()
obj.get_a()