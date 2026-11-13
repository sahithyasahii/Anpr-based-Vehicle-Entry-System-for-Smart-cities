import sqlite3

conn = sqlite3.connect("vehicle_logs.db")
cursor = conn.cursor()

# Create known_visitors table
cursor.execute("""
CREATE TABLE IF NOT EXISTS known_visitors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plate_number TEXT UNIQUE NOT NULL
)
""")

#Add a few known visitor plates
known_plates = ["KA03XY1234", "DL8CAF9999", "MH12KQ1111"]
for plate in known_plates:
    try:
        cursor.execute("INSERT INTO known_visitors (plate_number) VALUES (?)", (plate,))
    except:
        pass  # ignore duplicates

conn.commit()
conn.close()
print("✅ known_visitors table initialized with sample plates.")
