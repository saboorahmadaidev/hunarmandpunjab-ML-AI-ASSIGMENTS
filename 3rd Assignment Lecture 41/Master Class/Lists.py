# Master Class — Lists examples
my_list = [1,2,3,4,5]
print('Items:')
for item in my_list:
    print(item)

# demonstrate immutability of tuple using conversion
my_tuple = tuple(my_list)
print('Tuple from list:', my_tuple)
try:
    my_tuple[0] = 10
except TypeError as e:
    print('Cannot modify tuple:', e)
