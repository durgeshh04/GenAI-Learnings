# This section covers python List i.e Array we called in other programming language

names = ["Tiger", "Eagle", "Honey Bagger"]

print(f"List: {names}")

# adding name in list
names.append("Lion")
print(f"new list: {names}")

# extending list
food = ["pizza", "burger", "cold coffee"]
names.extend(food);
print(f"New List: {names}")

# insert element
names.insert(2, "Crow")

print(names)

# deleting element
poppedEl = names.pop()
print(poppedEl)
print(names)

# Check element is present or not
print(f"Checking is the Eagle is present inside the list or not:", "Eagle" in names)

# index
print(names.index("Eagle"))