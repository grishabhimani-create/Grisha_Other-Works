# Dictionary of 3 students

students = {
    "Student1": {"name": "Amit", "age": 18, "marks": 85},
    "Student2": {"name": "Priya", "age": 19, "marks": 92},
    "Student3": {"name": "Rahul", "age": 18, "marks": 78}
}

# Print student details
for student, details in students.items():
    print(student)
    print("Name:", details["name"])
    print("Age:", details["age"])
    print("Marks:", details["marks"])
    print()
