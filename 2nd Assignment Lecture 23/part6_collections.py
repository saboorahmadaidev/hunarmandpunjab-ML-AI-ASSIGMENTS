# Part 6 — Lists, Tuples & Sets
# List of 5 items
items = ['apple', 'banana', 'cherry', 'date', 'elderberry']
for it in items:
    print(it)

# Tuple and immutability
t = (1, 2, 3)
print('Tuple:', t)
# t[0] = 10  # This would raise TypeError — tuples are immutable

# Set operations
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print('Union ->', s1 | s2)
print('Intersection ->', s1 & s2)
print('Difference ->', s1 - s2)
