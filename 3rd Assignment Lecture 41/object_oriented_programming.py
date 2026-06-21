# object_oriented_programming.py
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}")

s = Student('Aamir', 18, 'B')
s.display()
