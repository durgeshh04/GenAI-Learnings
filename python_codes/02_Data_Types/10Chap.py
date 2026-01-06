order = dict(category = "Clothes", type = "Tshirt", size = "L", price = 450)

print(f"Your order: {order}")

# accessing a value of dict
print(f"Category of your order: {order["category"]}")

# creating dict with new way

order2 = {}
order2['category'] = "Electronics"
order2['type'] = "TV"

print(f"New order: {order2}")