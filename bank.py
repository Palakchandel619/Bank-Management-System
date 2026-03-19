from account import Account

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_no, name, pin):
        if acc_no in self.accounts:
            print("Account already exists")
            return

        if len(str(pin)) != 4:
            print("PIN must be 4 digits")
            return

        self.accounts[acc_no] = Account(acc_no, name, pin)
        print("Account created successfully")

    def get_account(self, acc_no, pin):
        account = self.accounts.get(acc_no)

        if not account:
            print("Account not found")
            return None

        if not account.validate_pin(pin):
            print("Incorrect PIN")
            return None

        return account