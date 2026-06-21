# Part 3 — Data Structures
# List
fruits = ['apple','banana','cherry']
print('List:', fruits)
fruits.append('date')
print('After append:', fruits)
fruits.remove('banana')
print('After remove:', fruits)

# Tuple (immutable)
t = (1,2,3)
print('Tuple:', t)

# Set operations
s1 = {1,2,3}
s2 = {3,4,5}
print('Union:', s1 | s2)
print('Intersection:', s1 & s2)
print('Difference:', s1 - s2)

# Dictionary
student = {'name':'Sara', 'age':20, 'grade':'A'}
print('Student:', student)
student['grade'] = 'A+'
print('Updated grade:', student['grade'])

# CRUD operations example on list of students
students = []
# Create
students.append({'name':'Ali','marks':80})
# Read
for s in students:
    print(s)
# Update
students[0]['marks'] = 85
# Delete
students.pop(0)
print('Students after delete:', students)
