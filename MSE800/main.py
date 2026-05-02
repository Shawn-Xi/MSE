from database import create_all_tables
from user_manager import add_user, view_users, update_user_status
from currency_manager import add_currency, view_currencies, update_exchange_rate
from user_wallet_manager import add_user_wallet, view_user_wallets, update_wallet_balance
from exchange_transaction_manager import add_exchange_transaction, view_user_transactions, update_transaction_status
from admin_staff_manager import add_admin_staff, view_admin_staff, update_admin_role
from rate_update_log_manager import add_rate_update_log, view_rate_update_logs
import datetime

def user_menu():
    while True:
        print("\n==== User Manager ====")
        print("1. Add User")
        print("2. View All Users")
        print("3. Update User Status")
        print("4. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            full_name = input("Enter full name: ")
            email = input("Enter email: ")
            phone_number = input("Enter phone number: ")
            password_hash = "some_hash"  # In a real app, this would be a secure hash
            registration_date = datetime.date.today()
            user_status = "Active"
            add_user(full_name, email, phone_number, password_hash, registration_date, user_status)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            user_id = int(input("Enter user ID: "))
            new_status = input("Enter new status (Active, Inactive, Banned): ")
            update_user_status(user_id, new_status)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

def currency_menu():
    while True:
        print("\n==== Currency Manager ====")
        print("1. Add Currency")
        print("2. View All Currencies")
        print("3. Update Exchange Rate")
        print("4. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            currency_code = input("Enter currency code (e.g., USD): ")
            currency_name = input("Enter currency name: ")
            country = input("Enter country: ")
            current_exchange_rate = float(input("Enter current exchange rate: "))
            rate_updated_time = datetime.datetime.now()
            decimal_precision = int(input("Enter decimal precision: "))
            add_currency(currency_code, currency_name, country, current_exchange_rate, rate_updated_time, decimal_precision)
        elif choice == '2':
            currencies = view_currencies()
            for currency in currencies:
                print(currency)
        elif choice == '3':
            currency_code = input("Enter currency code: ")
            new_rate = float(input("Enter new exchange rate: "))
            rate_updated_time = datetime.datetime.now()
            update_exchange_rate(currency_code, new_rate, rate_updated_time)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

def user_wallet_menu():
    while True:
        print("\n==== User Wallet Manager ====")
        print("1. Add User Wallet")
        print("2. View User Wallets")
        print("3. Update Wallet Balance")
        print("4. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            user_id = int(input("Enter user ID: "))
            currency_code = input("Enter currency code: ")
            balance = float(input("Enter balance: "))
            created_at = datetime.datetime.now()
            last_transaction_time = created_at
            add_user_wallet(user_id, currency_code, balance, created_at, last_transaction_time)
        elif choice == '2':
            user_id = int(input("Enter user ID to view wallets for: "))
            wallets = view_user_wallets(user_id)
            for wallet in wallets:
                print(wallet)
        elif choice == '3':
            wallet_id = int(input("Enter wallet ID: "))
            new_balance = float(input("Enter new balance: "))
            last_transaction_time = datetime.datetime.now()
            update_wallet_balance(wallet_id, new_balance, last_transaction_time)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

def exchange_transaction_menu():
    while True:
        print("\n==== Exchange Transaction Manager ====")
        print("1. Add Exchange Transaction")
        print("2. View User Transactions")
        print("3. Update Transaction Status")
        print("4. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            user_id = int(input("Enter user ID: "))
            from_currency_code = input("Enter from currency code: ")
            to_currency_code = input("Enter to currency code: ")
            exchange_amount = float(input("Enter exchange amount: "))
            fee_amount = float(input("Enter fee amount: "))
            transaction_time = datetime.datetime.now()
            transaction_status = "Pending"
            add_exchange_transaction(user_id, from_currency_code, to_currency_code, exchange_amount, fee_amount, transaction_time, transaction_status)
        elif choice == '2':
            user_id = int(input("Enter user ID to view transactions for: "))
            transactions = view_user_transactions(user_id)
            for transaction in transactions:
                print(transaction)
        elif choice == '3':
            transaction_id = int(input("Enter transaction ID: "))
            new_status = input("Enter new status (Pending, Completed, Failed): ")
            update_transaction_status(transaction_id, new_status)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

def admin_staff_menu():
    while True:
        print("\n==== Admin Staff Manager ====")
        print("1. Add Admin Staff")
        print("2. View All Admin Staff")
        print("3. Update Admin Role")
        print("4. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            admin_name = input("Enter admin name: ")
            admin_email = input("Enter admin email: ")
            role = input("Enter role (Super Admin, Manager, Editor): ")
            login_password = "secure_password" # In a real app, this would be a secure hash
            join_date = datetime.date.today()
            department = input("Enter department: ")
            add_admin_staff(admin_name, admin_email, role, login_password, join_date, department)
        elif choice == '2':
            admins = view_admin_staff()
            for admin in admins:
                print(admin)
        elif choice == '3':
            admin_id = int(input("Enter admin ID: "))
            new_role = input("Enter new role: ")
            update_admin_role(admin_id, new_role)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

def rate_update_log_menu():
    while True:
        print("\n==== Rate Update Log Manager ====")
        print("1. Add Rate Update Log")
        print("2. View Logs for a Currency")
        print("3. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            currency_code = input("Enter currency code: ")
            admin_id = int(input("Enter admin ID: "))
            old_rate = float(input("Enter old rate: "))
            new_rate = float(input("Enter new rate: "))
            update_timestamp = datetime.datetime.now()
            update_note = input("Enter update note: ")
            add_rate_update_log(currency_code, admin_id, old_rate, new_rate, update_timestamp, update_note)
        elif choice == '2':
            currency_code = input("Enter currency code to view logs for: ")
            logs = view_rate_update_logs(currency_code)
            for log in logs:
                print(log)
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

def main():
    create_all_tables()
    while True:
        print("\n==== Main Menu ====")
        print("1. User Manager")
        print("2. Currency Manager")
        print("3. User Wallet Manager")
        print("4. Exchange Transaction Manager")
        print("5. Admin Staff Manager")
        print("6. Rate Update Log Manager")
        print("7. Exit")
        choice = input("Select a manager: ")

        if choice == '1':
            user_menu()
        elif choice == '2':
            currency_menu()
        elif choice == '3':
            user_wallet_menu()
        elif choice == '4':
            exchange_transaction_menu()
        elif choice == '5':
            admin_staff_menu()
        elif choice == '6':
            rate_update_log_menu()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
