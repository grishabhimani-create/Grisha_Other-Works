# Count vowels, consonants, spaces, and words

sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0
spaces = 0

for ch in sentence:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch == " ":
        spaces += 1

words = len(sentence.split())

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", spaces)
print("Words:", words)
