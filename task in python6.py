# 1. Convert a Float to an Int
original_float = 15.75
float_to_int = int(original_float)

print("--- Float to Int ---")
print(f"Original: {original_float} (Type: {type(original_float).__name__})")
print(f"Converted: {float_to_int} (Type: {type(float_to_int).__name__})")


# 2. Convert an Int to a String
original_int = 100
int_to_str = str(original_int)

print("\n--- Int to String ---")
print(f"Original: {original_int} (Type: {type(original_int).__name__})")
print(f"Converted: '{int_to_str}' (Type: {type(int_to_str).__name__})")


# 3. Convert a String to a Float
original_str = "42.58"
str_to_float = float(original_str)

print("\n--- String to Float ---")
print(f"Original: '{original_str}' (Type: {type(original_str).__name__})")
print(f"Converted: {str_to_float} (Type: {type(str_to_float).__name__})")
