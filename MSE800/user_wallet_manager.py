import sqlite3
from database import create_connection

def add_user_wallet(user_id, currency_code, balance, created_at, last_transaction_time):
    """Adds a new user wallet to the UserWallet table."""
    sql = """INSERT INTO UserWallet (user_id, currency_code, balance, created_at, last_transaction_time)
             VALUES (?, ?, ?, ?, ?)"""
    with create_connection() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (user_id, currency_code, balance, created_at, last_transaction_time))
            conn.commit()
            print("User wallet added successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

def view_user_wallets(user_id):
    """Retrieves all wallets for a specific user."""
    sql = "SELECT * FROM UserWallet WHERE user_id = ?"
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (user_id,))
        return cursor.fetchall()

def update_wallet_balance(wallet_id, new_balance, last_transaction_time):
    """Updates the balance of a user wallet."""
    sql = "UPDATE UserWallet SET balance = ?, last_transaction_time = ? WHERE wallet_id = ?"
    with create_connection() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (new_balance, last_transaction_time, wallet_id))
            conn.commit()
            print("Wallet balance updated successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
