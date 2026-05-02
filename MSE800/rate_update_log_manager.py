import sqlite3
from database import create_connection

def add_rate_update_log(currency_code, admin_id, old_rate, new_rate, update_timestamp, update_note):
    """Adds a new rate update log to the RateUpdateLog table."""
    sql = """INSERT INTO RateUpdateLog (currency_code, admin_id, old_rate, new_rate, update_timestamp, update_note)
             VALUES (?, ?, ?, ?, ?, ?)"""
    with create_connection() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (currency_code, admin_id, old_rate, new_rate, update_timestamp, update_note))
            conn.commit()
            print("Rate update log added successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

def view_rate_update_logs(currency_code):
    """Retrieves all rate update logs for a specific currency."""
    sql = "SELECT * FROM RateUpdateLog WHERE currency_code = ?"
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (currency_code,))
        return cursor.fetchall()
