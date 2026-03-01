shopping_list = [
    {"item": "Milk", "price": 50},
    {"item": "Bread", "price": 30},
    {"item": "Eggs", "price": 60},
    {"item": "Rice", "price": 120}
]

# -------- Task 1: Add and Remove Items --------

# Add Butter
shopping_list.append({"item": "Butter", "price": 80})

# Remove first item
shopping_list.pop(0)

# Print number of items
print("Total items now:", len(shopping_list))


# -------- Task 2: Calculate Total Cost --------

# Calculate total cost
total_cost = sum(item["price"] for item in shopping_list)

# Find most expensive item
most_expensive = max(shopping_list, key=lambda x: x["price"])

print("Most expensive item:", most_expensive["item"], "-", most_expensive["price"])
print("Total cost:", total_cost)


# -------- Task 3: Create Summary Dictionary --------

total_items = len(shopping_list)
average_price = round(total_cost / total_items, 2)

summary = {
    "total_items": total_items,
    "total_cost": total_cost,
    "average_price": average_price
}

print("Summary:", summary)