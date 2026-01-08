import sqlite3

# Connect to the database
conn = sqlite3.connect('ev_network.db')
cursor = conn.cursor()

# List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:")
for table in tables:
    print(table[0])

# Example: Query stations table
print("\nStations:")
cursor.execute("SELECT * FROM stations LIMIT 5;")
stations = cursor.fetchall()
for station in stations:
    print(station)

# Close the connection
conn.close()
