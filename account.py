from transaction import transaction

class Account:
    def __init__(self, acc_no, name, pin):
        self.__acc_no = acc_no
        self.__name = name
        self.__balance = 0
        self.__pin = pin
        self.__transactions = []

    def validate_pin(self, pin):
        return self.__pin == pin

    def deposit(self, amount):
        if amount <= 0:
            print(" Invalid amount")
            return

        self.__balance += amount
        self.__transactions.append(transaction("Deposit", amount))
        print(f"{amount} deposited successfully")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return

        if amount > self.__balance:
            print("Insufficient balance")
            return

        self.__balance -= amount
        self.__transactions.append(transaction("Withdraw", amount))
        print(f"{amount} withdrawn successfully")

    def check_balance(self):
        print(f"Balance: {self.__balance}")

    def show_transactions(self):
        if not self.__transactions:
            print("No transactions yet")
            return

        print("\n Transaction History:")
        for t in self.__transactions:
            print(t)

    def get_acc_no(self):
        return self.__acc_no

    def get_name(self):
        return self.__name