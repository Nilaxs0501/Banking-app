def Customer():
    Name=input("Enter your Name:")
    Nic_num=input("Enter your Nic number:")
    Username=input("Enter your username:")
    Password=input("Enter your password:")
    return Customer
def Deposit():
    try:
        amount= float(input("Enter deposit amount: "))
        if amount<=0:
            print("invalid deposit amount")
        balance+=amount
        print(f"sucessfully deposited{amount}.New balance is {balance}")
        return balance
    
    except ValueError:
        print("please enter the valid amount.")

def Withdraw():
         try:
            amount= float(input("Enter withdraw amount: "))
            if amount<=0:
                 print("invalid withdraw amount")
            elif amount > balance:
                 print("insufficient balance")
            else:    
                 balance-=amount
            print(f"sucessfully withdraw{amount}.New balance is {balance}")
            return balance
         except ValueError:
            print("please enter the valid amount.")
 
    


def Customer_Creation():
    try:
        balance = float(input("Enter initial deposit amount: "))
        if balance > 0:
            username = balance
            print(f"Account for {username} created New balance is: {balance}")
        else:
            print("Enter the valid deposit amount.")
    except ValueError:
        print("Invalid amount.")
def view_transactions ():
    print("view transaction history :" )
#====================================ADMIN================================================
def admin_menu():
    while True:
        print("\nAdmin Menu")
        print("1. New customer create")
        print("2. Add new customer account")
        print("3. Deposit to customer account")
        print("4. Withdraw from customer account")
        print("5.View balance ")
        print("6. View Transaction History")
        print("7. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            print("\nCustomer Accounts:")
            Customer()
        elif choice == '2':
            Customer_Creation()
        elif choice == '3':
             Deposit()

        elif choice == '4':
                 Withdraw()

        elif choice == '7':
            print("Logging out from admin account.")
            break
        else:
            print("Invalid choice. Please try again.")
#================================CUSTOMER CREATION======================================
def customer_menu(Bank_accounts,username):
    while True:
        print(f"\nWelcome {username}")
        print("1. View balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. View Transaction History")
        print("5. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            print(f"Your balance is:Bank_accounts{ {username}}")
        elif choice == '2':
            try:
                amount = float(input("Enter deposit amount: "))
                if amount <= 0:
                    print("Deposit amount must be positive.")
                else:
                   Bank_accounts [username] += amount
                print(f"{amount} deposited. New balance is: {username}")
            except ValueError:
                print("Invalid amount.")
        elif choice == '3':
            try:
                amount = float(input("Enter withdrawal amount: "))
                if amount <= 0:
                    print("Withdrawal amount must be positive.")
                elif amount > [username]:
                    print("Insufficient balance.")
                else:
                    Bank_accounts[username] -= amount
                    print(f"{amount} withdrawn. New balance is: {username}")
            except ValueError:
                print("Invalid amount.")
        elif  choice=='4':
                 view_transactions()
        elif choice == '5':
            print(f"Logging out {username}.")
            break
        else:
            print("Invalid choice. Please try again.")
#============================MAIN FUNCTION=================================
def main():
    Bank_accounts={}
    
    while True:
        print("\nWelcome to Mini Banking System")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username=input("Enter admin username:")
            password = input("Enter admin password: ")
            if password == "1234" and username == "admin":
                admin_menu()
            else:
                print("Incorrect password.")
        elif choice == '2':
            username = input("Enter your username: ")
            if username in Bank_accounts:
                customer_menu( Bank_accounts, username)
            else:
                print("Account does not exist. Please contact admin to create an account.")
        elif choice == '3':
            print("Thank you for using the Mini Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()







