import numpy

arr = numpy.array([])

for i in range(10):
    num = int(input("Enter number to square"))
    arr = numpy.append(arr, num)

print(arr)

for i in arr:
    print(f"{i} and {i}square is {i*i}")