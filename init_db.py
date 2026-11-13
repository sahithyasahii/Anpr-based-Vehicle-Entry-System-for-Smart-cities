# init_db.py

import sqlite3

conn = sqlite3.connect('apartment.db')
cursor = conn.cursor()

# Create residents table
cursor.execute('''
CREATE TABLE IF NOT EXISTS residents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plate_number TEXT UNIQUE NOT NULL
)
''')

# Create visit_log table
cursor.execute('''
CREATE TABLE IF NOT EXISTS visit_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plate_number TEXT NOT NULL,
    status TEXT NOT NULL,
    timestamp TEXT NOT NULL
)
''')

conn.commit()
conn.close()
print("✅ Database initialized with residents and visit_log tables.")
