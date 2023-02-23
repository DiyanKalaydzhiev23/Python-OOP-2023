#  ((pizza, 2.50), (pizza, 7.50), (ice-cream, 5))
# {pizza:2.50, ice-cream:5}

data = (("pizza", 2.50), ("pizza", 7.50), ("ice-cream", 5))

data_dict = {}

for key, value in data:
    if key not in data_dict:
        data_dict[key] = value

print(data_dict)