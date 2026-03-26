import sqlite3

conn = sqlite3.connect("Database/hospital.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(treatments);")
print(cursor.fetchall())