physics = int(input("Enter your physics score: "))
chemistry = int(input("Enter your chemistry score: "))
maths = int(input("Enter your maths score: "))

total = physics + chemistry + maths

average =total/3

sentence = f"Hi, your marks in physics = {physics}, chemistry = {chemistry}, maths = {maths}. Your total marks is {total} and the average marks is {average}"
print(sentence)