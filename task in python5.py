# Taking two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing arithmetic operations
addition       = num1 + num2
subtraction    = num1 - num2
multiplication = num1 * num2
division       = num1 / num2 if num2 != 0 else "Undefined (cannot divide by zero)"
floor_division = num1 // num2 if num2 != 0 else "Undefined"
modulus        = num1 % num2 if num2 != 0 else "Undefined"
exponent       = num1 ** num2

# Displaying the results
print("\n--- 🧮 Arithmetic Results ---")
print(f"Addition ({num1} + {num2})         = {addition}")
print(f"Subtraction ({num1} - {num2})      = {subtraction}")
print(f"Multiplication ({num1} * {num2})   = {multiplication}")
print(f"Normal Division ({num1} / {num2})  = {division}")
print(f"Floor Division ({num1} // {num2}) = {floor_division}")
print(f"Modulus/Remainder ({num1} % {num2}) = {modulus}")
print(f"Exponentiation ({num1} ** {num2})  = {exponent}")
