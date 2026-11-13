# view_logs.py
import sqlite3
import pandas as pd

conn = sqlite3.connect('apartment_vehicles.db')
df = pd.read_sql_query("SELECT * FROM entry_logs", conn)
conn.close()

print(df)

