import sqlite3

conn = sqlite3.connect("logins.db")
cursor = conn.cursor()

print("Suspicious IPs with more than 2 failed login attempts:")
query = """
SELECT ip_address, COUNT(*) as attempts
FROM login_logs
WHERE status = 'failed'
GROUP BY ip_address
HAVING attempts > 2
"""

for row in cursor.execute(query):
    print(f"IP: {row[0]} | Failed Attempts: {row[1]}")

conn.close()
