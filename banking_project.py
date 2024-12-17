#banking program
def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to be deposited: "))
    if amount < 0:
        print("That is not a valid amount")
        return 0
    else:
        print(f"You have deposited ${amount:.2f}")
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient Funds")
        return 0
    elif amount < 0:
        print("Amount should be greater than zero")
        return 0
    else:
        print(f"You have withdrawn ${amount:.2f}")
        return amount

def main():
    balance = 0.0
    running = True

    while running:  # Running will remain True until the user chooses to exit
        print("\n************************")
        print("Banking Program")
        print("************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")        
        print("4. Exit")
        print("************************")
        choice = int(input("Enter a choice between (1-4): "))
          
        

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            print("Thank you for using the banking program. Goodbye!")
            running = False
        else:
            print("ENTER A CHOICE BETWEEN 1 TO 4")


main()
