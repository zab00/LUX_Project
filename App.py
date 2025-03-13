import psycopg2

# Database connection parameters
conn = psycopg2.connect(
    host="localhost",
    database="postgress",
    user="root",
    password="@amalma"
)

# Create a cursor object
cursor = conn.cursor()

# Execute a SELECT query
cursor.execute("SELECT * FROM employee")

# Fetch all rows
rows = cursor.fetchall()

# Print each row
for row in rows:
    print(row)

# Close cursor and connection
cursor.close()
conn.close()