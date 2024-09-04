import sqlite3

# Connect to the SQLite database (this will create a new file if it doesn't exist)
conn = sqlite3.connect('new_database.db')
cur = conn.cursor()

# Create a new table
cur.execute('''
CREATE TABLE IF NOT EXISTS studies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
