import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    passwd="root",
    user="root"
)

mycursor = db.cursor()

try:
    mycursor.execute('CREATE DATABASE IF NOT EXISTS alx_book_store')
    print("Database 'alx_book_store' created successfully!")

except:
    mysql.connector.Error

mycursor.close()
db.close()
