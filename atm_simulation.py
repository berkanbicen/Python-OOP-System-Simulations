import time

class Account:
    """Represents a bank account with secure balance management."""
    def __init__(self, card_number, pin, initial_balance=0):
        self._card_number = card_number
        self._pin = pin
        self._balance = initial_balance  # Encapsulation: Protected attribute

    def validate_pin(self, input_pin):
        return self._pin == input_pin

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"✅ Successfully deposited ${amount}. New Balance: ${self._balance}")
        else:
            print("❌ Invalid amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"✅ Successfully withdrew ${amount}. New Balance: ${self._balance}")
        else:
            print("❌ Insufficient funds or invalid amount.")

class ATM:
    """Manages the ATM interface and user interaction."""
    def __init__(self):
        # Database of dummy accounts
        self.accounts = {
            "123456": Account("123456", "1234", 1000),
            "987654": Account("987654", "0000", 500)
        }

    def start(self):
        print("\n=== WELCOME TO OOP BANK ATM ===")
        card_num = input("Enter Card Number: ")
        
        account = self.accounts.get(card_num)
        
        if account:
            pin = input("Enter PIN: ")
            if account.validate_pin(pin):
                self.run_session(account)
            else:
                print("❌ Wrong PIN.")
        else:
            print("❌ Card not found.")

    def run_session(self, account):
        print("\nLogin Successful!")
        while True:
            print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
            choice = input("Select Transaction: ")

            if choice == '1':
                print(f"💰 Current Balance: ${account.balance}")
            elif choice == '2':
                amt = float(input("Amount to deposit: "))
                account.deposit(amt)
            elif choice == '3':
                amt = float(input("Amount to withdraw: "))
                account.withdraw(amt)
            elif choice == '4':
                print("👋 Thank you for using OOP Bank.")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    atm = ATM()
    atm.start()