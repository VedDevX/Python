class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited ₹{amount}. New Balance: ₹{self.balance}")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient balance.")
        elif amount <= 0:
            print("❌ Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"✅ Withdrawn ₹{amount}. New Balance: ₹{self.balance}")
            
    def check_balance(self):
        print(f"💰 Current Balance: ₹{self.balance}")
        

def show_menu():
    print("\n🏦 Bank Account Menu")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

def main():
    print("=== Welcome to Bank Account Simulator ===")
    account_number = input("Enter Account Number: ")
    account_holder = input("Enter Account Holder Name: ")

    account = BankAccount(account_number, account_holder, 0)
    
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            amount = float(input("Enter the deposit amount: "))
            account.deposit(amount)
            
        elif choice == "2":
            amount = float(input("Enter the withdraw amount: "))
            account.withdraw(amount)
            
        elif choice == "3":
            account.check_balance()
            
        elif choice == "4":
            print("👋 Exiting. Thank you for using Bank Account Simulator!")
            break
        
        else:
            print("❌ Invalid choice. Please enter 1-4.")
            
if __name__ == "__main__":
    main()