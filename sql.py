import sqlite3

DB_NAME = "data_base.db"

def create_clients_table():
    """Створює таблицю clients, якщо вона ще не існує."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            posluha TEXT NOT NULL,
            marka TEXT NOT NULL,
            city TEXT NOT NULL,
            time TEXT NOT NULL,
            date TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def insert_client(posluha, marka, city, time):
    """Додає нового клієнта в базу даних."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO clients (posluha, marka, city, time) 
        VALUES (?, ?, ?, ?)
    ''', (posluha, marka, city, time))
    conn.commit()
    conn.close()
