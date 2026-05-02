import sqlite3
from database import create_connection

def add_exchange_transaction(user_id, from_currency_code, to_currency_code, exchange_amount, fee_amount, transaction_time, transaction_status):
    """Adds a new exchange transaction to the ExchangeTransaction table."""
    sql = """INSERT INTO ExchangeTransaction (user_id, from_currency_code, to_currency_code, exchange_amount, fee_amount, transaction_time, transaction_status)
             VALUES (?, ?, ?, ?, ?, ?, ?)"""
    with create_connection() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (user_id, from_currency_code, to_currency_code, exchange_amount, fee_amount, transaction_time, transaction_status))
            conn.commit()
            print("Exchange transaction added successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

def view_user_transactions(user_id):
    """Retrieves all transactions for a specific user."""
    sql = "SELECT * FROM ExchangeTransaction WHERE user_id = ?"
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (user_id,))
        return cursor.fetchall()

def update_transaction_status(transaction_id, new_status):
    """Updates the status of an exchange transaction."""
    sql = "UPDATE ExchangeTransaction SET transaction_status = ? WHERE transaction_id = ?"
    with create_connection() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (new_status, transaction_id))
            conn.commit()
            print("Transaction status updated successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
