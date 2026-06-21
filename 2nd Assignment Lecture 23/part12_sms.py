# Part 12 — Mini Student Management System (text-file persistence)
import json
DB = 'students_db.txt'

def load_students():
    students = []
    try:
        with open(DB, 'r') as f:
            for line in f:
                students.append(json.loads(line))
    except FileNotFoundError:
        pass
    return students

def save_students(students):
    with open(DB, 'w') as f:
        for s in students:
            f.write(json.dumps(s) + '\n')

def add_student():
    name = input('Name: ')
    age = input('Age: ')
    grade = input('Grade: ')
    students = load_students()
    students.append({'name': name, 'age': age, 'grade': grade})
    save_students(students)
    print('Student added')

def view_students():
    students = load_students()
    if not students:
        print('No students')
        return
    for i, s in enumerate(students, 1):
        print(i, s)

def update_student():
    students = load_students()
    view_students()
    idx = int(input('Enter student number to update: ')) - 1
    if 0 <= idx < len(students):
        students[idx]['name'] = input('New name: ')
        students[idx]['age'] = input('New age: ')
        students[idx]['grade'] = input('New grade: ')
        save_students(students)
        print('Updated')
    else:
        print('Invalid index')

def delete_student():
    students = load_students()
    view_students()
    idx = int(input('Enter student number to delete: ')) - 1
    if 0 <= idx < len(students):
        students.pop(idx)
        save_students(students)
        print('Deleted')
    else:
        print('Invalid index')

def menu():
    while True:
        print('\n1.Add 2.View 3.Update 4.Delete 5.Exit')
        choice = input('Choice: ')
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            break
        else:
            print('Invalid')

if __name__ == '__main__':
    menu()
