import mysql.connector

dataBase = mysql.connector.connect(
    
    host = 'localhost',
    user = 'root',
    passwd = '123@123'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE summarizerDB")

print("Done")