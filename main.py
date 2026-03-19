from bank import Bank

bank = Bank()

while True:
    print("\n====== BANK SYSTEM ======")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        acc_no = input("Enter Account Number: ")
        name = input("Enter Name: ")
        pin = int(input("Set 4-digit PIN: "))
        bank.create_account(acc_no, name, pin)

    elif choice in ["2", "3", "4", "5"]:
        acc_no = input("Enter Account Number: ")
        pin = int(input("Enter PIN: "))

        account = bank.get_account(acc_no, pin)
        if not account:
            continue

        if choice == "2":
            amount = float(input("Enter amount: "))
            account.deposit(amount)

        elif choice == "3":
            amount = float(input("Enter amount: "))
            account.withdraw(amount)

        elif choice == "4":
            account.check_balance()

        elif choice == "5":
            account.show_transactions()

    elif choice == "6":
        print("Thank you for using Bank System")
        break

    else:
        print("Invalid choice")