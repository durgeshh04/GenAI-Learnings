names = set()

print(f"Before adding values: {id(names)}")

names.add("Durgesh")

print(f"After adding first value: {id(names)}")   # Id is common even after changes happen in the set

names.add("Eagle")

print(f"After adding another value: {id(names)}")   # Id is common

print(f"Set of values: {names}")

# Primitive: "int, float, str, bool", Immutable, "If you ""change"" it, Python creates a new object with a new ID."
# Collections: "tuple, frozenset", Immutable, "Even though they hold multiple items, you cannot change them after creation."
# Non-Primitive: "list, dict, set", Mutable, "You can add, remove, or change items without changing the object's ID."