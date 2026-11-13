# setup_database.py

import sqlite3

# Connect to database (or create if not exists)
conn = sqlite3.connect('apartment_vehicles.db')
cursor = conn.cursor()

# Table 1: Registered residents
cursor.execute('''
CREATE TABLE IF NOT EXISTS registered_vehicles (
    plate TEXT PRIMARY KEY
)
''')

# Table 2: Entry logs
cursor.execute('''
CREATE TABLE IF NOT EXISTS entry_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plate TEXT,
    timestamp TEXT,
    status TEXT
)
''')

conn.commit()
conn.close()
print("✅ Database and tables set up successfully.")
