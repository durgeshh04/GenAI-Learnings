order = dict(category = "Clothes", type = "Tshirt", size = "L", price = 450)

print(f"Your order: {order}")

# accessing a value of dict
print(f"Category of your order: {order["category"]}")

# creating dict with new way

order2 = {}
order2['category'] = "Electronics"
order2['type'] = "TV"
order2["price"] = 13000
print(f"New order: {order2}")
del order2["price"]
print(f"New order: {order2}")

print(f"price is available for order 1? {"price" in order}")

# methods to fetch the dictionary values, keys and items:

print(f"keys of dict: {order.keys()}")
print(f"value of the dict: {order.values()}")
print(f"items of the dict: {order.items()}")


# Iterating through the dictionary

for key, val in order.items():
    print(f"{key}: {val}")