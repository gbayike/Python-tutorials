a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

def greatest(a,b,c):
    if (a > b and a > c):
        print(str(a) + " is the greatest")
    elif b > a and b > c:
        print(str(b) + " is the greatest")
    else:
        print(str(c) + " is the greatest")

greatest(a,b,c)