import time
from abc import ABC, abstractmethod
from typing import Dict, Optional

# ==============================================================================
## SECTION 1: CUSTOM EXCEPTIONS (Security & Integrity)
# ==============================================================================
class BankingError(Exception):
    """Base exception for all banking operations."""
    pass

class InvalidPinError(BankingError):
    """Raised when PIN verification fails."""
    pass

class InsufficientFundsError(BankingError):
    """Raised when an account lacks the necessary balance."""
    pass

class AccountNotFoundError(BankingError):
    """Raised when the card/account ID does not exist."""
    pass

# ==============================================================================
## SECTION 2: ACCOUNT ARCHITECTURE (Abstraction & Encapsulation)
# ==============================================================================

class BaseAccount(ABC):
    """Abstract Base Class defining core banking behavior."""
    def __init__(self, card_number: str, pin: str, initial_balance: float = 0.0):
        self._card_number = card_number
        self._pin = pin
        self._balance = initial_balance # Encapsulation

    @property
    def balance(self) -> float:
        return self._balance

    def validate_pin(self, input_pin: str) -> bool:
        return self._pin == input_pin

    @abstractmethod
    def withdraw(self, amount: float):
        """Must be implemented to handle specific withdrawal rules."""
        pass

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

class StandardAccount(BaseAccount):
    """A standard bank account with basic rules."""
    def withdraw(self, amount: float):
        if amount > self._balance:
            raise InsufficientFundsError(f"Requested: ${amount} | Available: ${self._balance}")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        
        self._balance -= amount

# ==============================================================================
## SECTION 3: BANKING INTERFACE (Business Logic)
# ==============================================================================

class ArasakaATM:
    """Manages secure transactions and user interface."""
    def __init__(self, terminal_id: str):
        self._terminal_id = terminal_id
        # Secure Vault (In-memory database simulation)
        self._vault: Dict[str, BaseAccount] = {
            "77-V": StandardAccount("77-V", "2077", 5000.0),
            "88-JACKIE": StandardAccount("88-JACKIE", "1010", 1500.0)
        }

    def authenticate(self, card_num: str, pin: str) -> BaseAccount:
        account = self._vault.get(card_num)
        if not account:
            raise AccountNotFoundError("Access Denied: Serial number not found.")
        if not account.validate_pin(pin):
            raise InvalidPinError("Access Denied: Biometric/PIN mismatch.")
        return account

    def start_terminal(self):
        print(f"\n{'='*10} ARASAKA BANKING TERMINAL [{self._terminal_id}] {'='*10}")
        card_num = input("Insert Credchip (Serial ID): ")
        pin = input("Enter Security PIN: ")

        try:
            active_account = self.authenticate(card_num, pin)
            self._session_loop(active_account)
        except BankingError as e:
            print(f"🔴 SECURITY ALERT: {e}")

    def _session_loop(self, account: BaseAccount):
        print(f"\nWelcome back, User. Link Established.")
        while True:
            print("\n1. Balance | 2. Deposit | 3. Withdraw | 4. Disconnect")
            choice = input("Select Action: ")

            try:
                if choice == '1':
                    print(f"💰 Available Credits: ${account.balance:.2f}")
                elif choice == '2':
                    amt = float(input("Amount to transfer to vault: "))
                    account.deposit(amt)
                    print(f"✅ Vault updated. New balance: ${account.balance:.2f}")
                elif choice == '3':
                    amt = float(input("Amount to withdraw: "))
                    account.withdraw(amt)
                    print(f"✅ Credits dispensed. New balance: ${account.balance:.2f}")
                elif choice == '4':
                    print("📡 Disconnecting... Stay safe in Night City.")
                    break
            except (InsufficientFundsError, ValueError) as e:
                print(f"⚠️ Transaction Failed: {e}")

# ==============================================================================
# DEVELOPER NOTE: DEMO CREDENTIALS
# To test the system, you can use the following pre-registered Serial IDs:
# 1. ID: 77-V       | PIN: 2077 (High Balance)
# 2. ID: 88-JACKIE  | PIN: 1010 (Standard Balance)
# ==============================================================================
# ==============================================================================
## EXECUTION
# ==============================================================================
if __name__ == "__main__":
    terminal = ArasakaATM("NC-CENTER-01")
    terminal.start_terminal()
