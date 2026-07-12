# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person constructor called")


# Child class
class Student(Person):
    def __init__(self, name, age, roll_no):
        # Call parent class constructor
        super().__init__(name, age)
        self.roll_no = roll_no
        print("Student constructor called")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)


# Create object
student = Student("Grisha", 20, 101)

# Display details
student.display()
