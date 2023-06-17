dict = {}
for i in range(5):
    prod = input("Enter product name: ")
    price = int(input("Enter price: "))
    dict[prod] = price

for k,v in dict.items():
    print(str(k) +":"+ str(v))