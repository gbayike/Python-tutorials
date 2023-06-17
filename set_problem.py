st = set()

for i in range(5):
    el = int(input("Enter a number to add to the set: "))
    el_set = {el}
    st.update(el_set)
sum = 0
prod = 1
for i in st:
    sum+=i
    prod*=i
    print(i)
print(sum)
print(prod)