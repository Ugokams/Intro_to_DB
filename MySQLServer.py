# MySQLServer.py

import mysql.connector
from mysql.connector import Error


def main():
    try:
        # Connect to MySQL server (without specifying a database)
        conn = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password'
        )
        cursor = conn.cursor()

        # Create the database only if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        # Check if creation affected something
        if cursor.rowcount >= 0:
            print("Database 'alx_book_store' created successfully!")

    except Error as err:
        print(f"Error: {err}")

    finally:
        # Clean up resources
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()


if __name__ == "__main__":
    main()
