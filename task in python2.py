# Function using *args to calculate sum

def find_sum(*args):
    total = 0

    for num in args:
        total += num

    return total

# Function call
result = find_sum(10, 20, 30, 40, 50)

print("Sum =", result)
