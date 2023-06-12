num = int(input("Enter number for table: "))
def table(num):
    i = 10
    while i>0:
        print(str(num) +" * "+ str(i) + " = " + str(num*i))
        i-=1

table(num)