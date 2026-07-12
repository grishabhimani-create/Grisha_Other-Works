# List of dictionaries for 5 products

products = [
    {"name": "Laptop", "price": 50000, "qty": 5},
    {"name": "Mobile", "price": 25000, "qty": 10},
    {"name": "Headphones", "price": 3000, "qty": 15},
    {"name": "Keyboard", "price": 1500, "qty": 20},
    {"name": "Monitor", "price": 12000, "qty": 8}
]

# Find the most expensive product
most_expensive = products[0]

for product in products:
    if product["price"] > most_expensive["price"]:
        most_expensive = product

# Print the most expensive product
print("Most Expensive Product:")
print("Name:", most_expensive["name"])
print("Price:", most_expensive["price"])
print("Quantity:", most_expensive["qty"])
