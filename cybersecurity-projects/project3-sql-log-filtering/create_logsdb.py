import sqlite3

# Connect to SQLite database (creates one if not exists)
conn = sqlite3.connect("logins.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS login_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    ip_address TEXT,
    status TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

# Sample data (some successful, some failed attempts)
logs = [
    ('admin', '192.168.1.10', 'failed'),
    ('admin', '192.168.1.10', 'failed'),
    ('user1', '10.0.0.5', 'success'),
    ('hacker1', '202.54.1.22', 'failed'),
    ('hacker1', '202.54.1.22', 'failed'),
    ('hacker1', '202.54.1.22', 'failed'),
    ('admin', '192.168.1.10', 'success'),
    ('user2', '172.16.0.2', 'success'),
    ('unknown', '202.54.1.22', 'failed'),
]

cursor.executemany("INSERT INTO login_logs (username, ip_address, status) VALUES (?, ?, ?)", logs)
conn.commit()
conn.close()


