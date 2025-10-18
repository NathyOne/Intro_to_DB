import mysql.connector
from mysql.connector import Error

# --- Connection Parameters ---
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "root"  # Use 'password', not 'passwd'


def create_database():
    """
    Connects to MySQL and attempts to create the specified database.
    """
    try:
        db = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )

        if db.is_connected():
            mycursor = db.cursor()
            mycursor.execute(f"CREATE DATABASE IF NOT EXISTS alx_book_store")
            print(f"Database 'alx_book_store' created successfully!")
            mycursor.close()
            db.close()
        else:
            print("Failed to connect to MySQL server.")
    except mysql.connector.Error:
        print(f"Error while connecting to MySQL or creating database: {e}")


create_database()
