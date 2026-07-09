import mysql.connector

def getConnection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="roottoor",
        database="user_db",
        port=3306
    )
    return connection


