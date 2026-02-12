rows = int(input("Enter number of rows: "))

print("\n--- Star Pattern ---")
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

print("\n--- Number Pattern ---")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n--- Alphabet Pattern ---")
for i in range(1, rows + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
