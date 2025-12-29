# This section is all about Tuple

names = ("Tiger", "Eagle", "Wolf", "Honey Bagger")

print(f"My tuple: {names}")

(name1, name2, name3, name4) = names    # If you don't extract tuples properly to the length then it will throw error: (name1, name2, name3) = names
                                        # ValueError: too many values to unpack (expected 3)

print(f"{name1}, {name2}, {name3}, {name4}")