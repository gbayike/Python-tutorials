fruits = ("apple", "banana", "cherry", "orange")

print(fruits[1])

for i in range(len(fruits)):
    print(fruits[i])

for fruit in fruits:
    print(fruit)

print(len(fruits))


if "orange" in fruits:
    print("orange in fruits")

# slicing

new_fruits = fruits[:2]
print(f"The new fruit is {new_fruits}")

# unpacking
person = ("John", 25, "male")

name, age, gender = person

print("Name:", name)

print("Age:", age)

print("Gender:", gender)