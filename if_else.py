def odd_even(n):
    if(n%2 != 0):
        print("alpha")
    elif(n%2 == 0 and n in range(5,10)):
        print("beta")
    elif(n%2 == 0 and n in range(10,20)):
        print("gamma")
    elif(n%2 == 0 and n > 45):
        print("delta")


n = int(input("Enter a number"))
odd_even(n)