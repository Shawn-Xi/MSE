import sqlite3
import random
import string
import os

# --- Define the absolute path for the database ---
# This ensures the DB is always found in the same directory as the script.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, 'usersl.db')

def get_db_connection():
    """Establishes a connection to the database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def login(email, password):
    """
    Checks user credentials against the database.
    Returns True if login is successful, False otherwise.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()
        
        if user:
            print("✅ Login successful!")
            return True
        else:
            print("❌ Login failed: Invalid email or password.")
            return False
            
    except sqlite3.Error as e:
        print(f"Database error during login: {e}")
        return False
    finally:
        if conn:
            conn.close()

def forgot_password(email):
    """
    Generates a password reset code, stores it, and simulates sending an email.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        
        if user:
            # Generate a random 6-digit code
            reset_code = ''.join(random.choices(string.digits, k=6))
            
            # Store the reset code in the database
            cursor.execute("UPDATE users SET reset_code = ? WHERE email = ?", (reset_code, email))
            conn.commit()
            
            # --- Email Simulation ---
            # In a real application, you would use a library like smtplib to send an email.
            # For this example, we just print the code to the console.
            print("\n--- SIMULATING EMAIL ---")
            print(f"To: {email}")
            print(f"Subject: Your Password Reset Code")
            print(f"Your password reset code is: {reset_code}")
            print("------------------------\n")
            print("📧 A password reset code has been 'sent' to your email.")
            return True
        else:
            print("❌ User with that email does not exist.")
            return False

    except sqlite3.Error as e:
        print(f"Database error during password reset request: {e}")
        return False
    finally:
        if conn:
            conn.close()

def reset_password(email, code, new_password):
    """
    Resets the password if the provided code is correct.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users WHERE email = ? AND reset_code = ?", (email, code))
        user = cursor.fetchone()
        
        if user:
            # Code is correct, update the password and clear the reset code
            cursor.execute("UPDATE users SET password = ?, reset_code = NULL WHERE email = ?", (new_password, email))
            conn.commit()
            print("✅ Password has been successfully reset!")
            return True
        else:
            print("❌ Invalid email or reset code.")
            return False
            
    except sqlite3.Error as e:
        print(f"Database error during password reset: {e}")
        return False
    finally:
        if conn:
            conn.close()

def main_menu():
    """
    A simple command-line interface to demonstrate the login system.
    """
    # First, ensure the database is set up.
    # In a real app, you might run this separately.
    from user_database_setup import setup_database
    setup_database()
    
    while True:
        print("\n==== Main Menu ====")
        print("1. Login")
        print("2. Forgot Password")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            login(email, password)
        
        elif choice == '2':
            email = input("Enter your email to reset password: ")
            if forgot_password(email):
                code = input("Enter the 6-digit code you received: ")
                new_password = input("Enter your new password: ")
                reset_password(email, code, new_password)

        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main_menu()
