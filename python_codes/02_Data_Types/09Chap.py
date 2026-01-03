set1 = {"n1", "n2", "n3"}
set2 = {"n4", "n2", "n5"}

union_set = set1 | set2    # set1.union(set2)
print(f"Union of sets: {union_set}")

intersection_set = set1 & set2
print(f"Intersection of sets: {intersection_set}")

only_in_set1 = set1 - set2
print(f"Only available in set1: {only_in_set1}")

# Check avaibility
print(f"n4 is present in set2?: {"n4" in set2}")

new_set = set()
# add data using add method
new_set.add("n6")
# use update to add data from other sets
new_set.update(set1)
new_set.update(set2)
# delete 
print(f"new set: {new_set}")
new_set.remove("n6")
print(f"new set: {new_set}")
new_set.pop()
print(f"new set: {new_set}")
