class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks   # Private variable

    # Getter method
    def get_marks(self):
        return self.__marks

    # Setter method
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks! Enter marks between 0 and 100.")

# Create object
student = Student("Grisha", 85)

# Get private variable
print("Student Name:", student.name)
print("Marks:", student.get_marks())

# Update marks using setter
student.set_marks(92)
print("Updated Marks:", student.get_marks())
