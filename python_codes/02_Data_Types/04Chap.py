# This file is all about boolean Data type in python

# We use True and False for handling boolean related operations in python


is_boiling = True
milk_price = 50

# upcasting: converting lower datatype into upper datatype
upcasting_result = milk_price + is_boiling
print(upcasting_result)


# Logical Operations: 
#There are three logical operators in python: and, or, not

# Example of and operator
if 1 == 1 and 2 == 2:
    print(True)
else: 
    print(False)

# Example of or operator
if 1 == 1 or 2 == -1:
    print(True)
else: 
    print(False)