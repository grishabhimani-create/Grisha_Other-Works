# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound")


# Child class Dog
class Dog(Animal):
    def sound(self):
        print(self.name, "says: Woof! Woof!")


# Child class Cat
class Cat(Animal):
    def sound(self):
        print(self.name, "says: Meow! Meow!")


# Create objects
dog = Dog("Buddy")
cat = Cat("Kitty")

# Call methods
dog.sound()
cat.sound()
