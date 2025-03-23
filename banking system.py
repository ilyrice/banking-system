class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f'Withdrew ${amount}. Current balance: ${self.balance}')
            else:
                print(f'Insufficient funds. Current balance: ${self.balance}')
        else:
            print("Withdraw amount must be positive.")

    def check_balance(self):
        print(f'Current balance: ${self.balance}')

def main():
    account = BankAccount('Atittaya', 6969)

    while True:
        print('\n--- Banking System ---')
        print('1. Deposit')
        print('2. Withdraw')
        print('3. Check Balance')
        print('4. Exit')

        choice = input('Choose an option:')

        if choice == '1':
            amount = float(input("Enter amount to deposit: $"))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: $"))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Exiting the banking system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()