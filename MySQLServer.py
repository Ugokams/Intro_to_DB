# MySQLServer.py

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (adjust credentials as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Try to create the database
            try:
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as err:
                print(f"Error while creating database: {err}")

            cursor.close()

    except Error as err:
        print(f"Error connecting to the database server: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
