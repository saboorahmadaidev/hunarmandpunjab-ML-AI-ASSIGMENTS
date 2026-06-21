# Master Class\File_Handling.py — read/write examples
fn = 'students.txt'
# write
with open(fn, 'w') as f:
    f.write('Ali,ali@example.com,20\n')
    f.write('Sara,sara@example.com,21\n')
print('Wrote sample students.txt')
# read
with open(fn, 'r') as f:
    print('Content:')
    print(f.read())
# append
with open(fn, 'a') as f:
    f.write('New, new@example.com, 19\n')
print('Appended new student')
