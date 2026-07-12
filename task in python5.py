# Squares of even numbers from 1 to 20 using list comprehension

squares = [num ** 2 for num in range(1, 21) if num % 2 == 0]

print("Squares of even numbers:")
print(squares)
