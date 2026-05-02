import sqlite3
from database import create_connection

def add_admin_staff(admin_name, admin_email, role, login_password, join_date, department):
    """Adds a new admin staff to the AdminStaff table."""
    sql = """INSERT INTO AdminStaff (admin_name, admin_email, role, login_password, join_date, department)
             VALUES (?, ?, ?, ?, ?, ?)"""
    with create_connection() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (admin_name, admin_email, role, login_password, join_date, department))
            conn.commit()
            print("Admin staff added successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

def view_admin_staff():
    """Retrieves all admin staff from the AdminStaff table."""
    sql = "SELECT * FROM AdminStaff"
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

def update_admin_role(admin_id, new_role):
    """Updates the role of an admin staff."""
    sql = "UPDATE AdminStaff SET role = ? WHERE admin_id = ?"
    with create_connection() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (new_role, admin_id))
            conn.commit()
            print("Admin role updated successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
