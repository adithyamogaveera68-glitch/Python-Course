balance = 1000   

print("1. Deposit\n2. Withdraw\n3. Check Balance")

choice = input("Enter your choice: ")

if choice == "1":
    amount = float(input("Enter deposit amount: "))
    balance += amount   
    print("Amount Deposited:", amount)
    print("Updated Balance:", balance)

elif choice == "2":
    amount = float(input("Enter withdraw amount: "))
    if amount <= balance:
        balance -= amount
        print("Amount Withdrawn:", amount)
        print("Updated Balance:", balance)
    else:
        print("Insufficient Balance!")

elif choice == "3":
    print("Current Balance:", balance)

else:
    print("Invalid choice")