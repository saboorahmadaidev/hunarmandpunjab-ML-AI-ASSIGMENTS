# Part 11 — Object-Oriented Python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}")

class Teacher(Student):
    def __init__(self, name, age, grade, subject):
        super().__init__(name, age, grade)
        self.subject = subject

    def display(self):
        super().display()
        print(f"Subject: {self.subject}")

s = Student('Bilal', 21, 'A')
s.display()

t = Teacher('Mrs Khan', 35, 'N/A', 'Math')
t.display()
