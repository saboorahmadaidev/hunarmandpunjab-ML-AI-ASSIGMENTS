# Part 1 — Python Basics & Input/Output
print('Welcome to Python Basics')

# Read input from user
name = input('Enter your name: ')
print('Hello,', name)

# Basic arithmetic
a = float(input('Enter number a: '))
b = float(input('Enter number b: '))
print('a + b =', a + b)
print('a - b =', a - b)
print('a * b =', a * b)
print('a / b =', a / b if b != 0 else 'Infinity')

# Simple calculator
op = input('Choose operator (+ - * /): ')
if op == '+':
    print('Result:', a + b)
elif op == '-':
    print('Result:', a - b)
elif op == '*':
    print('Result:', a * b)
elif op == '/':
    if b != 0:
        print('Result:', a / b)
    else:
        print('Cannot divide by zero')
else:
    print('Unknown operator')
