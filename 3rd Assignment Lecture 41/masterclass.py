# masterclass.py — combined example using functions, loops, and OOP
class Counter:
    def __init__(self):
        self.count = 0
    def inc(self):
        self.count += 1

c = Counter()
for i in range(5):
    c.inc()
print('Counter after loop:', c.count)

# use function
def square(x):
    return x * x
print('Squares:', [square(i) for i in range(5)])
