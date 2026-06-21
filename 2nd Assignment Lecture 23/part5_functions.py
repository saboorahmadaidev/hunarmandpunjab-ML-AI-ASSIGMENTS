# Part 5 — Functions
# 1. Add two numbers
def add(a, b):
    return a + b

print("add(3,4)", add(3,4))

# 2. Check if number is prime

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

print("is_prime(17)", is_prime(17))
print("is_prime(18)", is_prime(18))

# 3. default args, *args, **kwargs

def greet(name, msg='Hello'):
    print(msg, name)

def summarize(*args):
    print('Sum args ->', sum(args))

def info(**kwargs):
    for k, v in kwargs.items():
        print(k, '=>', v)

print('\nExamples:')
greet('Ali')
greet('Sara', 'Welcome')
summarize(1,2,3,4)
info(name='Zain', age=22)
