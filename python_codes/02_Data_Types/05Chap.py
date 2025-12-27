# In this file we learned about string datatype


temp_var = "abcdefghijklmnopqrstuvwxyz"
print(temp_var)
print(temp_var[0:10])     # [start: end] --> end is exclusive. It don't includes in the res.
print(temp_var[0:10:3])   # [start: end: step]  --> step is used for escaping.
print(temp_var[:10])      # [0:10] --> it considers from zero if we don't specify any start value.
print(temp_var[10:])      # [10: till_last] --> it considers from given start to last element of the string.
print(temp_var[::-1])     # [::-1] --> is used to reverse the string.

encoded = temp_var.encode("utf-8")  # Used for encoding
print(encoded)
print(encoded.decode("utf-8"))      # Used for decoding
