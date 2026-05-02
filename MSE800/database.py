import sqlite3

def create_connection():
    conn = sqlite3.connect("exchange.db")
    return conn

def create_user_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name VARCHAR,
            email VARCHAR UNIQUE,
            phone_number VARCHAR,
            password_hash VARCHAR,
            registration_date DATE,
            user_status VARCHAR CHECK(user_status IN ('Active', 'Inactive', 'Banned'))
        )
    ''')
    conn.commit()
    conn.close()

def create_currency_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Currency (
            currency_code VARCHAR PRIMARY KEY,
            currency_name VARCHAR,
            country VARCHAR,
            current_exchange_rate DECIMAL,
            rate_updated_time DATETIME,
            decimal_precision INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def create_user_wallet_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS UserWallet (
            wallet_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            currency_code VARCHAR,
            balance DECIMAL,
            created_at DATETIME,
            last_transaction_time DATETIME,
            FOREIGN KEY (user_id) REFERENCES User (user_id),
            FOREIGN KEY (currency_code) REFERENCES Currency (currency_code)
        )
    ''')
    conn.commit()
    conn.close()

def create_exchange_transaction_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ExchangeTransaction (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            from_currency_code VARCHAR,
            to_currency_code VARCHAR,
            exchange_amount DECIMAL,
            fee_amount DECIMAL,
            transaction_time DATETIME,
            transaction_status VARCHAR CHECK(transaction_status IN ('Pending', 'Completed', 'Failed')),
            FOREIGN KEY (user_id) REFERENCES User (user_id),
            FOREIGN KEY (from_currency_code) REFERENCES Currency (currency_code),
            FOREIGN KEY (to_currency_code) REFERENCES Currency (currency_code)
        )
    ''')
    conn.commit()
    conn.close()

def create_admin_staff_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS AdminStaff (
            admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
            admin_name VARCHAR,
            admin_email VARCHAR UNIQUE,
            role VARCHAR CHECK(role IN ('Super Admin', 'Manager', 'Editor')),
            login_password VARCHAR,
            join_date DATE,
            department VARCHAR
        )
    ''')
    conn.commit()
    conn.close()

def create_rate_update_log_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS RateUpdateLog (
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            currency_code VARCHAR,
            admin_id INTEGER,
            old_rate DECIMAL,
            new_rate DECIMAL,
            update_timestamp DATETIME,
            update_note TEXT,
            FOREIGN KEY (currency_code) REFERENCES Currency (currency_code),
            FOREIGN KEY (admin_id) REFERENCES AdminStaff (admin_id)
        )
    ''')
    conn.commit()
    conn.close()

def create_all_tables():
    create_user_table()
    create_currency_table()
    create_user_wallet_table()
    create_exchange_transaction_table()
    create_admin_staff_table()
    create_rate_update_log_table()

if __name__ == '__main__':
    create_all_tables()
