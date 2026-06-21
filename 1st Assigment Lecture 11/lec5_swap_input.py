# LEC 5: Swap two variables without a third variable
# Using tuple unpacking; includes user input

a = input("Enter first value: ")
b = input("Enter second value: ")
print("Before swap: a=", a, "b=", b)

# swap without third variable
a, b = b, a
print("After swap: a=", a, "b=", b)
