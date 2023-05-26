def power(num, power):
    result = 1

    for i in range(power):
        result *= num


    return result

print(power(2,4))