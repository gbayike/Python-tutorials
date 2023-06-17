dict = {"red":6, "blue":82, "black":100, "white":89}
simple_dict = {k:v+3 for (k,v) in dict.items()}
print(simple_dict)

simple_dict_if = {k:v+3 for (k,v) in dict.items() if v%2 == 0}
print(simple_dict_if)

simple_dict_if_else = {k:("even" if v%2==0 else "odd") for (k,v) in dict.items()}
print(simple_dict_if_else)

simple_dict_nested_if = {k:v+3 for (k,v) in dict.items() if v%2 == 0 if v%3==0}
print(simple_dict_nested_if)