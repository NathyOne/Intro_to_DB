import mysql.connector


try:
    db = mysql.connector.connect(
        host="localhost",
        passwd="root",
        user="root"
    )
    if db.is_connected:
        mycursor = db.cursor()

        mycursor.execute('CREATE DATABASE IF NOT EXISTS alx_book_store')
        print("Database 'alx_book_store' created successfully!")
        mycursor.close()
        db.close()
    else:
        print("Failed to connect to MySQL server.")

except:
    mysql.connector.Error
