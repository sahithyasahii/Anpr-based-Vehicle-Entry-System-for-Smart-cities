import sqlite3
from datetime import datetime

# Connect to the database
conn = sqlite3.connect('apartment.db')  # Make sure this is the correct path
cursor = conn.cursor()

# Get all records where exit_time is NULL
cursor.execute("SELECT id FROM visit_log WHERE exit_time IS NULL")
rows = cursor.fetchall()

# Current simulated exit time
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Update each row with the current time as exit_time
for row in rows:
    visit_id = row[0]
    cursor.execute("UPDATE visit_log SET exit_time = ? WHERE id = ?", (current_time, visit_id))

conn.commit()
conn.close()

print(f"✅ Updated exit_time for {len(rows)} visitors to {current_time}")
