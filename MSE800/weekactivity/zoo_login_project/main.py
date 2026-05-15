from auth import admin_login


def main():
    """
    Main function to run the Zoo Admin Login application.
    """
    print("--- Welcome to the Zoo Management System ---")
    username = input("Enter username: ")
    password = input("Enter password: ")

    is_logged_in = admin_login(username, password)

    if is_logged_in:
        print("Access Granted. Welcome, Admin!")
    else:
        print("Access Denied. Please try again.")


if __name__ == "__main__":
    main()