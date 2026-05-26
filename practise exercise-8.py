# practice exercise

#Create a simple grading system

# Simple Grading System

# Get marks from the user
marks = float(input("Enter student marks (0-100): "))

# Determine grade
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

# Display result
print("Grade:", grade)
