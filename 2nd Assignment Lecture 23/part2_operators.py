# Part 2 — Operators & Expressions
x = 10
y = 3

# Arithmetic
print("+", x + y)
print("-", x - y)
print("*", x * y)
print("/", x / y)
print("%", x % y)
print("//", x // y)
print("**", x ** y)

# Comparison
print("==", x == y)
print("!=", x != y)
print("<", x < y)
print(">", x > y)

# Logical
print("and", x > 5 and y < 5)
print("or", x < 5 or y < 5)
print("not", not (x == y))

# Assignment
z = 5
z += 2
print("z after +=2", z)

# Bitwise
print("x & y", x & y)
print("x | y", x | y)
print("x ^ y", x ^ y)

# Expression with multiple operators
expr = (x + y) * (x - y) // y
print("expr ->", expr)
