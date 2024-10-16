# Initial balance for the user
balance = 0.0

# ATM menu
def atm_menu():
    print("Welcome to DTB Bank!")
    choice = int(input("Please select your options: "))
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")


created_acc = False

# Generate a new account

def create_account():
    global created_acc
    print("Creating a new account...")
    user_name = input("Enter your name: ")
    pin = input("Enter your PIN: ")
    print("Account created successfully!")
    created_acc = True
# Main ATM logic using if statements
def main():
    global balance  # Make balance accessible inside the function

    while True:
        atm_menu()  # Show the menu
        choice = input("Enter your choice: ")

        if choice == '1':
            # Deposit
            deposit_amount = float(input("Enter deposit amount: "))
            if deposit_amount > 0:
                balance += deposit_amount
                print(f"KES {deposit_amount} deposited successfully.")
            else:
                print("Deposit amount must be positive.")

        elif choice == '2':
            # Withdraw
            withdraw_amount = float(input("Enter withdrawal amount: "))
            if withdraw_amount > 0:
                if balance >= withdraw_amount:
                    balance -= withdraw_amount
                    print(f"KES {withdraw_amount} withdrawn successfully.")
                else:
                    print("Insufficient balance.")
            else:
                print("Withdrawal amount must be positive.")

        elif choice == '3':
            # Check Balance
            print(f"Your current balance is: KES {balance}")

        elif choice == '4':
            # Exit
            print("Thank you for using DTB ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


   
        