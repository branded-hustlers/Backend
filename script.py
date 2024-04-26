import mysql.connector

try:
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sylphlike",
        database="grocery_management_system"
    )

    # Check if the connection is successful
    if conn.is_connected():
        print("Connected to MySQL database!")

        # Perform a query to test the connection
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print("Tables in the database:")
        for table in tables:
            print(table)

        # Close cursor and connection
        cursor.close()
        conn.close()

    else:
        print("Failed to connect to MySQL database!")

except Exception as e:
    print("Error:", e)
