# Enter the number of elements
n = int(input("Enter the number of elements in the array: "))

# Create an empty list
arr = []

# Take elements as input
print("Enter the elements in the array:")
for i in range(n):
    element = int(input())
    arr.append(element)

# Find the mode
frequency = {}

for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Find element with maximum frequency
max_count = 0
mode = None

for key in frequency:
    if frequency[key] > max_count:
        max_count = frequency[key]
        mode = key

# Check if mode exists
if max_count > 1:
    print("The mode of the array is:", mode)
else:
    print("No mode found (all elements appear only once)")