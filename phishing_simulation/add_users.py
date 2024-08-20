import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('phishing_simulation.db')
cursor = conn.cursor()

# Create the users table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    clicked INTEGER DEFAULT 0,
    submitted INTEGER DEFAULT 0
)
''')

# Insert new user emails
users = [
    ('example3@gmail.com',),
    ('example2@gmail.com',),
    ('example1@gmail.com',)
]

cursor.executemany('INSERT INTO users (email) VALUES (?)', users)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Users have been added to the database.")
