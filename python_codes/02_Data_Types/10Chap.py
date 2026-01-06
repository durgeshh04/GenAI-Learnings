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