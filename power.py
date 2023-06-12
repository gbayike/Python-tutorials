import math


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

power1 = math.pow(num1, 3)
print("The first number is "+str(power1))
power2 = math.pow(num2,3)
print("The second number is "+str(power2))

sum = power1+power2
print("The sum is "+str(sum))