# Simulate a 1D array using a list

arr = [10, 20, 30, 40, 50]

print("Original Array:", arr)

# Insert an element
arr.append(60)
print("After Inserting 60:", arr)

# Delete an element
arr.remove(30)
print("After Deleting 30:", arr)

# Search for an element
search = int(input("Enter element to search: "))

if search in arr:
    print(search, "found in the array.")
else:
    print(search, "not found in the array.")
