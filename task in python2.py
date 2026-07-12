# Reverse a string using a loop

text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reversed string:", reverse)
