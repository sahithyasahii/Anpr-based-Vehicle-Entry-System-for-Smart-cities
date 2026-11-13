import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import random

# Load plates from CSV
df = pd.read_csv('cleaned_plates.csv')
plates = df['plate'].str.upper().str.strip().tolist()

# Connect to the database
conn = sqlite3.connect('apartment.db')
cursor = conn.cursor()

# Fetch registered residents
cursor.execute("SELECT plate_number FROM residents")
registered_plates = set(row[0].upper().strip() for row in cursor.fetchall())

# Set base date
base_date = datetime.strptime("2025-05-23", "%Y-%m-%d")

for plate in plates:
    # Random entry time
    entry_offset = random.randint(0, 1439)  # minutes in a day
    entry_time = base_date + timedelta(minutes=entry_offset)
    entry_str = entry_time.strftime("%Y-%m-%d %H:%M:%S")

    # Random exit time 10–180 minutes after entry
    exit_offset = random.randint(10, 180)
    exit_time = entry_time + timedelta(minutes=exit_offset)
    exit_str = exit_time.strftime("%Y-%m-%d %H:%M:%S")

    # Status: resident or visitor
    status = "resident" if plate in registered_plates else "visitor"
    log_icon = "🏠" if status == "resident" else "📌"
    print(f"{log_icon} Plate '{plate}' entered at {entry_str} and exited at {exit_str}")

    # Insert into DB
    cursor.execute('''
        INSERT INTO visit_log (plate_number, status, timestamp, exit_time)
        VALUES (?, ?, ?, ?)
    ''', (plate, status, entry_str, exit_str))

# Commit and close
conn.commit()
conn.close()
