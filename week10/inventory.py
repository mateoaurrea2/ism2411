# ISM2411 - Week 10 Lab: Lists
# Mateo Urrea
#
# Reflection
#
# 1. What surprised me most was that list methods like .sort() and .append()
#    change the original list directly instead of giving back a new one. I
#    expected to need to save the result into a new variable, but the list
#    just updates itself. Negative indexing was also a nice surprise since
#    grabbing the last item with [-1] is way easier than counting.
#
# 2. When I worked at Chick-fil-A, keeping track of item counts for restocking
#    was all done by hand or in a spreadsheet. If those counts were in a Python
#    list, I could loop through and pull out everything below a reorder level
#    in a few lines instead of scanning rows
#    and sorting columns in Excel every time.


# Exercise 1 - Build the list
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2 - Index practice
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

# Exercise 3 - Slicing
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4 - Modify
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# Exercise 5 - Tuple comparison
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError as e:
    print("TypeError caught:", e)
    print("Tuples are immutable, so coordinates can't be accidentally changed.")
print(coords)

# Exercise 6 - Average of a list of sales
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
print("Total:", total)
print("Count:", count)
print("Average:", total / count)
print("Best:", max(sales))
print("Worst:", min(sales))

# Exercise 7 - Accumulator pattern
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))
print(prices)
print(discounted)

# Exercise 8 - Filter above threshold
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for s in sales:
    if s > 300:
        high_sales.append(s)
print(high_sales)
print("Count:", len(high_sales))
print("Avg:", round(sum(high_sales) / len(high_sales), 2))
