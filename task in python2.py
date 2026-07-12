class BankAccount:
    # Constructor
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        print("Bank account created successfully!")

    # Display account details
    def display(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)

    # Destructor
    def __del__(self):
        print("Bank account deleted.")


# Create object
account = BankAccount("Grisha", 5000)

# Display details
account.display()

# Delete object
del account
