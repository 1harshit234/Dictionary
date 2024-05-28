sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
y = dict()

for i in keys:
     y.update({i:sample_dict[i]})
print(y)