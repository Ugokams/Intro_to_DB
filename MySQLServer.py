# MySQLServer.py

import mysql.connector

def create_database():
    try:
        # Connect to MySQL Server (update credentials accordingly)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # Replace with your actual MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            try:
                # Create database if it does not exist
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except mysql.connector.Error as db_err:
                print(f"Error while creating database: {db_err}")
            finally:
                cursor.close()

    except mysql.connector.Error as conn_err:
        print(f"Error connecting to the database server: {conn_err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
