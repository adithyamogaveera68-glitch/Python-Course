# Task 1
text = input("Enter a string: ")


freq = {}


for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1


print("Character Frequencies:")
for key in freq:
    print(key, ":", freq[key])

# Task 2


d = {}

n = int(input("Enter number of elements: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value


swapped = {}

for key in d:
    swapped[d[key]] = key

print("Original Dictionary:", d)
print("Swapped Dictionary:", swapped)