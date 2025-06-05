import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',         #  is blank
    database='mydatabase'      # database name
)

cursor = conn.cursor()

# Insert sample data
cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Johnzizi", "john@example.com"))
conn.commit()

# Fetch data
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

# Close connection
cursor.close()
conn.close()
