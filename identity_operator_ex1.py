num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("num1 is num2: " + str(num1 is num2))
print("num1 is not num2: " + str(num1 is not num2))

if(num1 is num2):
    print("num1 is num2")

else:
    print("num1 is not num2")