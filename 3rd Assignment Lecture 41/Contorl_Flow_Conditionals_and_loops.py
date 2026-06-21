# Part 2 — Control Flow & Loops
# if-elif-else example: check positive/negative/zero
n = int(input('Enter integer: '))
if n > 0:
    print('Positive')
elif n < 0:
    print('Negative')
else:
    print('Zero')

# Grading example
marks = int(input('Enter marks (0-100): '))
if marks >= 80:
    print('Grade A')
elif marks >= 60:
    print('Grade B')
elif marks >= 40:
    print('Grade C')
else:
    print('Fail')

# for loop: 1-10
print('\nFor loop 1-10:')
for i in range(1, 11):
    print(i, end=' ')
print('\n')

# while loop: even numbers up to 10
print('While loop evens:')
i = 2
while i <= 10:
    print(i, end=' ')
    i += 2
print('\n')

# break & continue demonstration
print('\nBreak & Continue:')
for i in range(1, 10):
    if i == 5:
        print('Skipping 5')
        continue
    if i == 8:
        print('Stopping at 8')
        break
    print(i)

# Nested loop: multiplication table (1-5)
print('\nMultiplication table:')
for a in range(1, 6):
    for b in range(1, 6):
        print(f"{a}x{b}={a*b}", end='\t')
    print()
