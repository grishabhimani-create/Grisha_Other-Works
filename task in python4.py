# Sort a list of tuples by the second element using lambda

students = [
    ("Amit", 85),
    ("Priya", 92),
    ("Rahul", 78),
    ("Neha", 88)
]

# Sort by the second element (marks)
students.sort(key=lambda x: x[1])

print("Sorted List:")
for student in students:
    print(student)
