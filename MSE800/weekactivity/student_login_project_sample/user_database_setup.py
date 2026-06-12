import sqlite3
import os

# --- Define the absolute path for the database ---
# This ensures the DB is created in the same directory as the script.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, 'usersl.db')

def setup_database():
    """
    Creates the usersl.db database and the users table in the script's directory.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Create the users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                reset_code TEXT
            )
        ''')
        
        print(f"Database '{os.path.basename(DB_PATH)}' and table 'users' created successfully at: {DB_PATH}")
        
        # --- Add Users ---
        users_to_add = [
            ('test@example.com', 'password123'),
            ('csu.wind@gmail.com', '123')
        ]
        
        for email, password in users_to_add:
            try:
                cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
                print(f"User '{email}' inserted.")
            except sqlite3.IntegrityError:
                print(f"User '{email}' already exists.")

        conn.commit()

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    setup_database()
