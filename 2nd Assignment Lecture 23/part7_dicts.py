# Part 7 — Dictionaries & Data Handling
student = {'name': 'Aisha', 'age': 19, 'grade': 'B'}
print('Student name:', student['name'])

# Update values
student['grade'] = 'A+'
student['roll'] = 101

# Loop through items
for k, v in student.items():
    print(k, '->', v)
