import numpy

arr = numpy.array([1,2,3,4,5,6,7,8,9,10])
# comprehension
# lst = [i for i in arr]
lst = arr.tolist()

print(lst)

sum = 0 
for i in lst:
    sum+=i
print(sum)