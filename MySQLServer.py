import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    passwd="root",
    user="root"
)

mycursor = db.cursor()

mycursor.execute('CREATE DATABASE IF NOT EXISTS alx_book_store')

mycursor.close()
db.close()
