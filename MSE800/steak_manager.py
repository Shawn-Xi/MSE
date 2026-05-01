from database import create_connection
import sqlite3

def add_steak(weight, price):
    """Adds a new steak to the steak table."""
    sql = "INSERT INTO steak (weight, price) VALUES (?, ?)"
    with create_connection() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (weight, price))
            conn.commit()
            print("✅ Steak added successfully.")
        except sqlite3.Error as e:
            print(f"❌ Database error: {e}")

def view_steaks():
    """Retrieves all steaks from the steak table."""
    sql = "SELECT * FROM steak"
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

def delete_steak(steak_id):
    """Deletes a steak from the steak table by its ID."""
    sql = "DELETE FROM steak WHERE id = ?"
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (steak_id,))
        conn.commit()
        print("🗑️ Steak deleted.")