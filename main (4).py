class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            print("Invalid deposit amount. Amount should be greater than 0.")
            return False

    def withdraw(self, amount):
        if amount > 0 and self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        else:
            print("Invalid withdrawal amount or insufficient balance.")
            return False

    def display_balance(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__account_holder_name}")
        print(f"Account Balance: ${self.__account_balance:.2f}")


# Testing the BankAccount class
if __name__ == "__main__":
    # Create an instance of BankAccount
    my_account = BankAccount("12345", "Monesh", 1000.0)

    # Display initial balance
    my_account.display_balance()

    # Deposit money
    my_account.deposit(500.0)

    # Display updated balance
    my_account.display_balance()

    # Withdraw money
    my_account.withdraw(300.0)

    # Display final balance
    my_account.display_balance()
