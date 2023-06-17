set = {"Aina", "Alan", "Bana", "Christiana", "Christian", "Christopher"}

new_set = {i for i in set if i.endswith("a")}
print(new_set)