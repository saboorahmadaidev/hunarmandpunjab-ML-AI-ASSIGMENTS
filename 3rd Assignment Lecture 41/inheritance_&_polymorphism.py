# inheritance_&_polymorphism.py
class Person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"Hi, I'm {self.name}")

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def speak(self):
        print(f"Student {self.name}, grade {self.grade}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def speak(self):
        print(f"Teacher {self.name}, subject {self.subject}")

# Demo
stu = Student('Faiza', 'A')
tea = Teacher('Mr. Ali', 'Physics')
stu.speak()
tea.speak()
