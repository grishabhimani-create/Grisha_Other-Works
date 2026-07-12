# Recursive function to calculate factorial

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# User input
num = int(input("Enter a number: "))

# Display result
print("Factorial =", factorial(num))
