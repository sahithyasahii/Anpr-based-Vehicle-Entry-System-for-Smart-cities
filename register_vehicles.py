# register_vehicles.py

import sqlite3

def register_vehicle(plate):
    conn = sqlite3.connect('apartment_vehicles.db')
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO registered_vehicles (plate) VALUES (?)", (plate,))
        conn.commit()
        print(f"✅ Vehicle '{plate}' registered successfully.")
    except sqlite3.IntegrityError:
        print(f"⚠️ Vehicle '{plate}' is already registered.")
    
    conn.close()


resident_plates = ["KA03MN1234", "KA05AB5678", "MH12CD3456"]
for plate in resident_plates:
    register_vehicle(plate)
