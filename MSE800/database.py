import sqlite3

def create_connection():
    conn = sqlite3.connect("student.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT
        )
    ''')
    conn.commit()
    conn.close()

def create_restaurant_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS restaurant (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT,
            boss TEXT,
            waiters INTEGER,
            boss_id INTEGER
        )
    ''')
    conn.commit()
    conn.close()
    create_steak_table()

def create_steak_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS steak (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            weight REAL NOT NULL,
            price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
