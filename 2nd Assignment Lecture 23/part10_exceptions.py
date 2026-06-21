# Part 10 — Exception Handling
# Division by zero
try:
    a = 10
    b = 0
    print('a / b =', a / b)
except ZeroDivisionError:
    print('Cannot divide by zero')

# Multiple exceptions
try:
    vals = [1,2,3]
    print(vals[5])
    x = int('abc')
except IndexError:
    print('Index error caught')
except ValueError:
    print('Value error caught')
except Exception as e:
    print('Other exception:', e)
