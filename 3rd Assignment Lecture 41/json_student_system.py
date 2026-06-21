# json_student_system.py — read/write JSON student data
import json
fn = 'student.json'

# read
with open(fn, 'r') as f:
    data = json.load(f)
print('Loaded students:', data)

# add a student and write back
new = {'name': 'NewStudent', 'age': 18, 'grade': 'C'}
data.append(new)
with open(fn, 'w') as f:
    json.dump(data, f, indent=2)
print('Added new student')
