# Case 1: Two variables pointing to the exact same value
x = 10
y = 10

print("--- Case 1: Same Values ---")
print(f"Memory ID of x: {id(x)}")
print(f"Memory ID of y: {id(y)}")
print(f"Do x and y point to the same memory? {id(x) == id(y)}")

# Case 2: Changing one variable to point to a different value
y = 20

print("\n--- Case 2: Different Values ---")
print(f"Memory ID of x: {id(x)}")
print(f"Memory ID of y: {id(y)}")
print(f"Do x and y point to the same memory? {id(x) == id(y)}")
