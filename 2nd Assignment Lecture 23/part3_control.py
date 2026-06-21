# Part 3 — Control Statements
# Check if number is positive, negative, or zero
n = int(input("Enter an integer: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# Simple grading system
marks = int(input("Enter marks (0-100): "))
if marks >= 85:
    grade = 'A'
elif marks >= 70:
    grade = 'B'
elif marks >= 50:
    grade = 'C'
else:
    grade = 'F'
print(f"Marks: {marks} -> Grade: {grade}")
