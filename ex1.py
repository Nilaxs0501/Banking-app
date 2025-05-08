#====================== Customer information===================
def Customer_info():
    Name = input("Enter your Name:")
    Nic_num = input("Enter your Nic number:")
    Username = input("Enter your username:")
    Password = input("Enter your password:")
    return [Name,Nic_num,Username,Password]

def Create_Customer_and_User():
    Customers = Customer_info()
with open("Customers.txt", "a") as file:
        file.write(f"{name},{nic},{username},{password}\n")

    with open("Customers.txt","a")as Customers_file:
        Customers_file.write(f"{Customers[0]},{Customers[1]}\n")

    with open("User.txt","a")as User_file:    
        User_file.write(f"{Customers[2]},{Customers[3]}\n")

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
 
def Account_creation():
    try:
        username = input("Enter username for new account: ")
        if username in User :
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
            Create_Customer_and_User()
        elif choice == '2':

        else:
            print("Invalid choice. Please try again.")
#================================CUSTOMER CREATION======================================
def customer_menu():
    while True:
        print(f"\nWelcome ")
        print("1. View balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. View Transaction History")
        print("5. Logout")
        choice = input("Enter choice: ")

       
#============================MAIN FUNCTION=================================
def main():
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
            if username in username :
                customer_menu ( )
            else:
                print("Account does not exist. Please contact admin to create an account.")
        elif choice == '3':
            print("Thank you for using the Mini Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()







