list1 = ["abc", "xyz", "pqr"]
list2 = ["uvw", "ijk"]
new_list = list1 + list2
print(f"{new_list}")


list2 = list2 * 3
print(f"{list2}")

raw_list = bytearray(b"Eagle")
print(f"{raw_list}")
raw_list = raw_list.replace(b"E", b"P")
print(f"{raw_list}")


str = "Hello Eagle, how are you?"
print(f"Length of the string: {len(str)}")