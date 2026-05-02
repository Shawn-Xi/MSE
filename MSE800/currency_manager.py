import sqlite3
from database import create_connection

def add_currency(currency_code, currency_name, country, current_exchange_rate, rate_updated_time, decimal_precision):
    """Adds a new currency to the Currency table."""
    sql = """INSERT INTO Currency (currency_code, currency_name, country, current_exchange_rate, rate_updated_time, decimal_precision)
             VALUES (?, ?, ?, ?, ?, ?)"""
    with create_connection() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (currency_code, currency_name, country, current_exchange_rate, rate_updated_time, decimal_precision))
            conn.commit()
            print("Currency added successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

def view_currencies():
    """Retrieves all currencies from the Currency table."""
    sql = "SELECT * FROM Currency"
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

def update_exchange_rate(currency_code, new_rate, rate_updated_time):
    """Updates the exchange rate of a currency."""
    sql = "UPDATE Currency SET current_exchange_rate = ?, rate_updated_time = ? WHERE currency_code = ?"
    with create_connection() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (new_rate, rate_updated_time, currency_code))
            conn.commit()
            print("Exchange rate updated successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
