import os

Bank_accounts = {}
Transaction_history = {}

def Customer_info():
    Name = input("Enter your Name: ")
    Nic_num = input("Enter your NIC number: ")
    Username = input("Enter your username: ")
    Password = input("Enter your password: ")
    return [Name, Nic_num, Username, Password]

def Create_Customer_and_User():
    customer = Customer_info()
    [name, nic, username, password ]=customer

    if username in Bank_accounts:
        print("Username already exists.")
        return

    Bank_accounts[username] = 0.0
    Transaction_history[username] = []

    with open("Customers.txt","a")as Customers_file:
        Customers_file.write(f"{[0]},{[1]}\n")

    with open("User.txt","a")as User_file:    
        User_file.write(f"{[2]},{[3]}\n")
    print(f"Customer {username} created successfully.")
    


    

def View_All_Customers():
    if not os.path.exists("Customers.txt"):
        print("No customers found.")
        return

    with open("Customers.txt", "r") as Customers_file:
        lines =  Customers_file.readlines()
        if lines:
            print("Customer Records:")
            for line in lines:
                print(line.strip())
        else:
            print("No customer data available.")

def Deposit(username):
    try:
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Invalid deposit amount.")
            return
        Bank_accounts[username] += amount
        Transaction_history[username].append(f"Deposited {amount}")
        print(f"Successfully deposited {amount}. New balance is {Bank_accounts[username]}")
    except ValueError:
        print("Please enter a valid amount.")

def Withdraw(username):
    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > Bank_accounts[username]:
            print("Insufficient balance.")
        else:
            Bank_accounts[username] -= amount
            Transaction_history[username].append(f"Withdrew {amount}")
            print(f"Successfully withdrew {amount}. New balance is {Bank_accounts[username]}")
    except ValueError:
        print("Please enter a valid amount.")

def Customer_Creation():
    try:
        username = input("Enter username for new account: ")
        if username in Bank_accounts:
            print("Account already exists.")
            return
        balance = float(input("Enter initial deposit amount: "))
        if balance > 0:
            Bank_accounts[username] = balance
            Transaction_history[username] = [f"Initial deposit {balance}"]
            print(f"Account created. New balance is: {balance}")
        else:
            print("Invalid deposit amount.")
    except ValueError:
        print("Invalid amount.")

def view_transactions(username):
    print("Transaction History:")
    for transaction in Transaction_history.get(username, []):
        print(transaction)
    with open("Transaction.txt","w")as Transaction_file:
            print(Transaction_file.readlines())



#============================= ADMIN ====================================
def admin_menu():
    while True:
        print("\nAdmin Menu")
        print("1. Create New Customer")
        print("2. Add New Customer Account")
        print("3. Deposit to Customer Account")
        print("4. Withdraw from Customer Account")
        print("5. View All Customers")
        print("6. View Transaction History")
        print("7. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            Create_Customer_and_User()
        elif choice == '2':
            Customer_Creation()
        elif choice == '3':
            user = input("Enter username: ")
            if user in Bank_accounts:
                Deposit(user)
            else:
                print("User not found.")
        elif choice == '4':
            user = input("Enter username: ")
            if user in Bank_accounts:
                Withdraw(user)
            else:
                print("User not found.")
        elif choice == '5':
            View_All_Customers()
        elif choice == '6':
            user = input("Enter username: ")
            if user in Bank_accounts:
                view_transactions(user)
            else:
                print("User not found.")
        elif choice == '7':
            print("Logging out from admin account.")
            break
        else:
            print("Invalid choice. Please try again.")

#============================ CUSTOMER ===================================
def customer_menu(username):
    while True:
        print(f"\nWelcome {username}")
        print("1. View balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. View Transaction History")
        print("5. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            print(f"Your balance is: {Bank_accounts[username]}")
        elif choice == '2':
            Deposit(username)
        elif choice == '3':
            Withdraw(username)
        elif choice == '4':
            view_transactions(username)
        elif choice == '5':
            print(f"Logging out {username}.")
            break
        else:
            print("Invalid choice. Please try again.")

#============================ MAIN FUNCTION ===============================
def main():
    while True:
        print("\nWelcome to Mini Banking System")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            if password == "1234" and username == "admin":
                admin_menu()
            else:
                print("Incorrect credentials.")
        elif choice == '2':
            username = input("Enter your username: ")
            if username in Bank_accounts:
                customer_menu(username)
            else:
                print("Account does not exist. Please contact admin to create an account.")
        elif choice == '3':
            print("Thank you for using the Mini Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()