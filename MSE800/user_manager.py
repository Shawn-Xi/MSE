import sqlite3
from database import create_connection

def add_user(full_name, email, phone_number, password_hash, registration_date, user_status):
    """Adds a new user to the User table."""
    sql = """INSERT INTO User (full_name, email, phone_number, password_hash, registration_date, user_status)
             VALUES (?, ?, ?, ?, ?, ?)"""
    with create_connection() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (full_name, email, phone_number, password_hash, registration_date, user_status))
            conn.commit()
            print("User added successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

def view_users():
    """Retrieves all users from the User table."""
    sql = "SELECT * FROM User"
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

def update_user_status(user_id, new_status):
    """Updates the status of a user."""
    sql = "UPDATE User SET user_status = ? WHERE user_id = ?"
    with create_connection() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (new_status, user_id))
            conn.commit()
            print("User status updated successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
