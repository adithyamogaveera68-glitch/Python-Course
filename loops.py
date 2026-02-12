num = int(input("Enter table number: "))
limit = int(input("Enter the limit: "))

print("\nUsing for loop:\n")

for i in range(1, limit + 1):
    print(f"{num} * {i} = {num * i}")


