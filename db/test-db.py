import psycopg2

# Replace with your actual values
host = '192.168.0.59'
port = 5432
database = 'postgres'
user = 'postgres'
password = 'Yeboyes#78'

# Connect to PostgreSQL
conn = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)
cur = conn.cursor()

# Example: Read data
cur.execute("SELECT * FROM newtable;")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()