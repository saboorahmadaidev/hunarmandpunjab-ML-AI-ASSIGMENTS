# Master Class\Funtions.py — reusable functions examples

def add(a, b):
    return a + b

def greet(name, msg='Hello'):
    return f"{msg}, {name}"

def sum_all(*args):
    return sum(args)

def print_info(**kwargs):
    return ', '.join(f"{k}={v}" for k, v in kwargs.items())

if __name__ == '__main__':
    print('add(2,3)=', add(2,3))
    print(greet('Ali'))
    print('sum_all:', sum_all(1,2,3))
    print('info:', print_info(name='A', age=20))
