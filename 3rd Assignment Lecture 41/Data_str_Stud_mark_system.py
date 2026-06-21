# Student mark system storing grades
students = []

def add_student(name, marks):
    grade = compute_grade(marks)
    students.append({'name': name, 'marks': marks, 'grade': grade})

def compute_grade(marks):
    if marks >= 85:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >= 50:
        return 'C'
    else:
        return 'F'

def view_students():
    for s in students:
        print(s)

# Demo
add_student('Ahmed', 90)
add_student('Nadia', 67)
view_students()
