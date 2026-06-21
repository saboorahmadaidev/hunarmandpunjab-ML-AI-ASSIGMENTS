# Master Class — Dictionaries examples
student = {'name':'Amina', 'age':21}
print('Name:', student.get('name'))
# update
student['age'] = 22
# loop
for k, v in student.items():
    print(k, '->', v)
