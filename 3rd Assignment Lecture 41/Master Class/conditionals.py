# Master Class — Conditionals examples
x = int(input('Enter number: '))
if x % 2 == 0:
    print('Even')
else:
    print('Odd')

# nested condition
if x > 0:
    if x % 2 == 0:
        print('Positive even')
    else:
        print('Positive odd')
else:
    print('Non-positive')
