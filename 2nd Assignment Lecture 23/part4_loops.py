# Part 4 — Loops & Iterations
# 1. Print numbers 1 to 20 using for loop
print("Numbers 1 to 20:")
for i in range(1, 21):
    print(i, end=' ')
print('\n')

# 2. Print even numbers using while loop
print("Even numbers up to 20:")
i = 2
while i <= 20:
    print(i, end=' ')
    i += 2
print('\n')

# 3. Nested loop: multiplication table (1-5)
print("\nMultiplication table 1 to 5:")
for a in range(1, 6):
    for b in range(1, 6):
        print(f"{a}x{b}={a*b}", end='\t')
    print()
