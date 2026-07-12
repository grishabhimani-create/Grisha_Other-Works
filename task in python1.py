# Function to return a greeting

def greet(name, age):
    return f"Hello {name}! You are {age} years old."

# User input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Call the function
message = greet(name, age)
print(message)
