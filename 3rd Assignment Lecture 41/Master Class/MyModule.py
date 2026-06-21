# Master Class\MyModule.py — simple custom module

def multiply(a, b):
    return a * b

def welcome(name):
    return f"Welcome, {name}!"

if __name__ == '__main__':
    print('multiply(3,4)=', multiply(3,4))
    print(welcome('Student'))
