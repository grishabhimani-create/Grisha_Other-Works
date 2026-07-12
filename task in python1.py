# Create Car class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print()


# Create two objects
car1 = Car("Toyota", "Fortuner", 2022)
car2 = Car("Honda", "City", 2021)

# Print details
car1.display()
car2.display()
