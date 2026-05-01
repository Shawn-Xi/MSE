from database import create_connection
import sqlite3

def add_restaurant(name, location, boss, waiters, boss_id):
    """Adds a new restaurant to the restaurant table."""
    sql = "INSERT INTO restaurant (name, location, boss, waiters, boss_id) VALUES (?, ?, ?, ?, ?)"
    with create_connection() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (name, location, boss, waiters, boss_id))
            conn.commit()
            print("✅ Restaurant added successfully.")
        except sqlite3.Error as e:
            print(f"❌ Database error: {e}")

def view_restaurants():
    """Retrieves all restaurants from the restaurant table."""
    sql = "SELECT * FROM restaurant"
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

def delete_restaurant(restaurant_id):
    """Deletes a restaurant from the restaurant table by its ID."""
    sql = "DELETE FROM restaurant WHERE id = ?"
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (restaurant_id,))
        conn.commit()
        print("🗑️ Restaurant deleted.")