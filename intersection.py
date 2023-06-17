set1 = set()
for i in range(5):
    num = int(input("Enter number: "))
    set1.add(num)
print(set1)

set2 = set()
for i in range(5):
    num = int(input("Enter number: "))
    set2.add(num)
print(set2)

print(set1.intersection(set2))