# Error_Handling.py — simple try/except example
try:
    x = int(input('Enter a number: '))
    print('Reciprocal:', 1 / x)
except ZeroDivisionError:
    print('Cannot divide by zero')
except ValueError:
    print('Invalid integer')
