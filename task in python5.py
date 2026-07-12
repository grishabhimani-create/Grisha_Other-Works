# Parent class
class Animal:
    def speak(self):
        print("Animal makes a sound")


# Child class
class Dog(Animal):
    def speak(self):
        print("Woof!")


# Create objects
animal = Animal()
dog = Dog()

# Call methods
animal.speak()
dog.speak()
