def add_numbers(num):
    result = 0
    for i in range(1, num+1):
        result += i
        print(i)
    print("the total number after addition is "+ str(result))


num = int(input("Enter number to add: "))
add_numbers(num)